import json
import time
import threading
import logging
import pika
import requests
from ftplib import FTP

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - Manager: %(message)s'
)


class ManagerNode:
    def __init__(self):

        # RabbitMQ connection settings
        self.rabbitmq_host = 'localhost'
        self.rabbitmq_queue = 'car_data'
        # Initialize RabbitMQ connection
        self.init_rabbitmq()

        # FTP connection settings
        self.ftp_host = 'localhost'
        self.ftp_user = 'ftpuser'
        self.ftp_pass = 'ftppass'
        self.ftp_check_interval = 30

        # Message queue for handling data
        self.message_queue = []
        self.message_queue_lock = threading.Lock()


    def init_rabbitmq(self):
        """Initialize RabbitMQ connection and channel"""
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=self.rabbitmq_host)
        )
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.rabbitmq_queue)

    def start(self):
        """Start all worker threads"""
        threads = [
            threading.Thread(target=self._run_listening_to_rabit_mq, daemon=True),
            threading.Thread(target=self._run_listening_to_ftp, daemon=True),
            threading.Thread(target=self._handle_messages, daemon=True)
        ]

        for thread in threads:
            thread.start()

        # Keep main thread alive
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("Shutting down Manager Node...")
            self.connection.close()

    def _handle_messages(self):
        """Message processing thread"""
        while True:
            if self.message_queue:
                with self.message_queue_lock:
                    message = self.message_queue.pop(0)

                if message['type'] == 'rabbitmq':
                    self._process_car_data(message['data'])
                elif message['type'] == 'ftp_file':
                    self._process_ftp_file(message['filename'])

            time.sleep(0.1)  # Prevent CPU spinning

    def _run_listening_to_ftp(self):
        """FTP polling thread"""
        while True:
            try:
                with FTP(self.ftp_host) as ftp:
                    ftp.login(self.ftp_user, self.ftp_pass)
                    # Check for new files
                    files = ftp.nlst()
                    for file in files:
                        if file.endswith('.json'):
                            self._handle_ftp_file(ftp, file)
            except Exception as e:
                print(f"FTP Error: {e}")

            time.sleep(self.ftp_check_interval)

    def _handle_ftp_file(self, ftp, filename):
        """Handle downloaded FTP file"""
        try:
            with open(f'temp_{filename}', 'wb') as temp_file:
                ftp.retrbinary(f'RETR {filename}', temp_file.write)

            # Add to message queue
            with self.message_queue_lock:
                self.message_queue.append({
                    'type': 'ftp_file',
                    'filename': f'temp_{filename}'
                })
        except Exception as e:
            print(f"Error handling FTP file {filename}: {e}")

    def _run_listening_to_rabit_mq(self):
        """Start the manager node"""
        print("Starting Manager Node...")
        print(f"Listening for car data on queue: {self.rabbitmq_queue}")

        # Set up RabbitMQ consumer
        self.channel.basic_consume(
            queue=self.rabbitmq_queue,
            on_message_callback=self._handle_rabbitmq_message,
            auto_ack=True
        )

        try:
            print("Manager Node is running. Press CTRL+C to exit.")
            self.channel.start_consuming()
        except KeyboardInterrupt:
            print("Shutting down Manager Node...")
            self.connection.close()

    def _handle_rabbitmq_message(self, ch, method, properties, body):
        """Handle incoming RabbitMQ message"""
        # try:
        data = json.loads(body)
        with self.message_queue_lock:
            self.message_queue.append({
                'type': 'rabbitmq',
                'data': data
            })
        # except json.JSONDecodeError as e:
        #     print(f"Error decoding RabbitMQ message: {e}")

    def _process_car_data(self, data):
        """Process and forward car data to leader"""
        target_server = self._get_current_target()
        # try:
        response = requests.post(
            f"{target_server}/car/",
            json=ManagerNode.transform_car_data(data)
        )
        print(f"Car data forwarded. Status: {response.status_code}")
        # except requests.RequestException as e:
        #     print(f"Error forwarding car data: {e}")

    def _process_ftp_file(self, filename):
        """Process and forward FTP file to leader"""
        target_server = self._get_current_target()
        # try:
        with open(filename, 'rb') as f:
            response = requests.post(
                f"{target_server}/car/files/",
                files={'file': f}
            )
        print(f"File forwarded. Status: {response.status_code}")
        # except requests.RequestException as e:
        #     print(f"Error forwarding file: {e}")

    def _get_current_target(self):
        """Get current target server (leader or default)"""
        return "http://localhost:8000"

    @staticmethod
    def transform_car_data(car_data):
        """Transform car data keys to match LAB2 schema"""
        key_mapping = {
            'Capacit. motor': 'capacit_motor',
            'Tip combustibil': 'tip_combustibil',
            'Anul fabricației': 'anul_fabricatiei',
            'Cutia de viteze': 'cutia_de_viteze',
            'Marcă': 'marca',
            'Modelul': 'modelul',
            'Tip tractiune': 'tip_tractiune',
            'Distanță parcursă': 'distanta_parcursa',
            'Tip caroserie': 'tip_caroserie',
            'price': 'price',
            'link': 'link'
        }

        transformed_data = {}
        for old_key, new_key in key_mapping.items():
            if old_key in car_data:
                # Convert price to string since schema expects string
                if new_key == 'price':
                    transformed_data[new_key] = str(car_data[old_key])
                else:
                    transformed_data[new_key] = car_data[old_key]

        return transformed_data



if __name__ == "__main__":
    manager = ManagerNode()
    manager.start()