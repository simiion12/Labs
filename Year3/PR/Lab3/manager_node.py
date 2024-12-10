import json
import time
import threading
import logging
import pika
import requests
from ftplib import FTP
from fastapi import FastAPI

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - Manager: %(message)s'
)


class ManagerNode:
    def __init__(self):
        # Create FastAPI app
        self.app = FastAPI()
        self.setup_routes()

        # RabbitMQ connection settings
        self.rabbitmq_host = 'iepure_MQ'
        self.rabbitmq_queue = 'car_data'
        self.connection = None
        self.channel = None

        if not self.init_rabbitmq():
            logging.warning("Initial RabbitMQ connection failed, will retry in background...")

        # FTP connection settings
        self.ftp_host = 'ftp_server'
        self.ftp_user = 'ftpuser'
        self.ftp_pass = 'ftppass'
        self.ftp_check_interval = 30

        # Message queue for handling data
        self.message_queue = []
        self.message_queue_lock = threading.Lock()

        # Leader election
        self.current_leader = None
        self.leader_port = None

    def setup_routes(self):
        @self.app.post("/update_leader")
        async def update_leader(server_id: str, port: int, term: int):
            self.current_leader = server_id
            self.leader_port = port
            print(f"Leader updated to {server_id} on port {port} with term {term}")
            return {"status": "success"}

    def _get_current_target(self) -> str:
        """Get current target server URL"""
        if self.current_leader and self.leader_port:
            return f"http://PR-Lab2-{self.current_leader.capitalize()}:{self.leader_port}"
        return f"http://PR-Lab2-Node1:8001"

    def init_rabbitmq(self, max_retries=5, initial_delay=1):
        """Initialize RabbitMQ connection with retry mechanism"""
        retry_count = 0
        while retry_count < max_retries:
            try:
                logging.info(f"Attempting to connect to RabbitMQ (attempt {retry_count + 1}/{max_retries})")
                self.connection = pika.BlockingConnection(
                    pika.ConnectionParameters(
                        host=self.rabbitmq_host,
                        connection_attempts=3,
                        retry_delay=2
                    )
                )
                self.channel = self.connection.channel()
                self.channel.queue_declare(queue=self.rabbitmq_queue)
                logging.info("Successfully connected to RabbitMQ")
                return True
            except pika.exceptions.AMQPConnectionError as e:
                retry_count += 1
                if retry_count == max_retries:
                    logging.error(f"Failed to connect to RabbitMQ after {max_retries} attempts: {e}")
                    return False
                wait_time = initial_delay * (2 ** retry_count)  # exponential backoff
                logging.info(f"Connection failed, retrying in {wait_time} seconds...")
                time.sleep(wait_time)

    def start(self):
        """Start all worker threads"""
        # First, try to establish RabbitMQ connection
        if not self.init_rabbitmq():
            print("Failed to establish initial RabbitMQ connection. Starting without it...")

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
        """RabbitMQ consumer thread"""
        while True:
            try:
                if not self.connection or self.connection.is_closed:
                    self.init_rabbitmq()

                if self.channel:
                    print("Starting to consume messages...")
                    self.channel.basic_consume(
                        queue=self.rabbitmq_queue,
                        on_message_callback=self._handle_rabbitmq_message,
                        auto_ack=True
                    )
                    self.channel.start_consuming()
            except Exception as e:
                print(f"RabbitMQ connection error: {e}")
                time.sleep(5)

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

    def get_app(self):
        """Return the FastAPI app instance"""
        return self.app

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
