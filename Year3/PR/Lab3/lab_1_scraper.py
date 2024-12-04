from Labs.Year3.PR.Lab1.parser import CarScraper
from Labs.Year3.PR.Lab1.web_utils import change_to_mdl_currency
import pika
import json
import tempfile
from ftplib import FTP


def send_to_ftp(data, filename="processed_cars.json"):
    try:
        # Create temporary file with the data
        with tempfile.NamedTemporaryFile(mode='w+', delete=False) as tmp_file:
            json.dump(data, tmp_file, indent=4)
            tmp_file_path = tmp_file.name

        # Connect to FTP server and send file
        ftp = FTP('localhost')
        ftp.login(user='ftpuser', passwd='ftppass')  # Updated credentials

        # Open and send the file
        with open(tmp_file_path, 'rb') as file:
            ftp.storbinary(f'STOR {filename}', file)

        print(f"Successfully uploaded {filename} to FTP server")
        ftp.quit()

    except Exception as e:
        print(f"FTP Error: {e}")



def publish_cars():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='car_data')

    base_url = "https://sargutrans.md/page/{}/"
    final_cars = []

    for i in range(1, 2):
        url = base_url.format(i)
        final_cars.extend(CarScraper(url).parse_page())

    for car in final_cars:
        print(car)
        channel.basic_publish(
            exchange='',
            routing_key='car_data',
            body=json.dumps(car)
        )

    connection.close()


    final_cars_mdl_currency = change_to_mdl_currency(final_cars)
    # Send to ftp server
    send_to_ftp(final_cars_mdl_currency)


if __name__ == "__main__":
    publish_cars()