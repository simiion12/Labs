import ssl
import socket
from urllib.parse import urlparse
from car import Car


def get_webpage(url, max_redirects=5):
    for _ in range(max_redirects):
        parsed_url = urlparse(url)
        host = parsed_url.netloc
        path = parsed_url.path if parsed_url.path else '/'
        port = 443 if parsed_url.scheme == 'https' else 80

        if parsed_url.scheme == 'https':
            context = ssl.create_default_context()
            with socket.create_connection((host, port)) as sock:
                with context.wrap_socket(sock, server_hostname=host) as secure_sock:
                    send_request(secure_sock, host, path)
                    response = receive_response(secure_sock)
        else:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((host, port))
                send_request(s, host, path)
                response = receive_response(s)

        headers, _, body = response.partition(b'\r\n\r\n')
        status_line = headers.split(b'\r\n')[0].decode()

        if status_line.startswith('HTTP/1.1 3') or status_line.startswith('HTTP/1.0 3'):
            location = next(
                line.split(': ')[1] for line in headers.decode().split('\r\n') if line.startswith('Location: '))
            url = location
        else:
            return body.decode()

    raise Exception("Too many redirects")


def send_request(sock, host, path):
    request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"
    sock.sendall(request.encode())


def receive_response(sock):
    response = b""
    while True:
        data = sock.recv(4096)
        if not data:
            break
        response += data
    return response


def get_car_objects_from_data(data):
    return [Car(d.get('Capacit. motor', 'N/A'), d.get('Tip combustibil', 'N/A'), d.get('Anul fabricației', 'N/A'),
                d.get('Cutia de viteze', 'N/A'), d.get('Marcă', 'N/A'), d.get('Modelul', 'N/A'),
                d.get('Tip tractiune', 'N/A'), d.get('Distanță parcursă', 'N/A'), d.get('Tip caroserie', 'N/A'),
                d.get('price', 0), d.get('link', 'N/A')) for d in data]


def save_json(cars, filename):
    json_output = Car.serialize_list_to_json(cars)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json_output)


def save_xml(cars, filename):
    xml_output = Car.serialize_list_to_xml(cars)
    with open('cars.xml', 'w', encoding='utf-8') as f:
        f.write(xml_output)


def read_json(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        json_content = f.read()

    car_list = Car.from_json(json_content)
    return car_list


def read_xml(filename):
    cars_list = []
    with open(filename, 'r', encoding='utf-8') as f:
        xml_content = f.read()

    car_entries = xml_content.split('</Car>')

    for entry in car_entries:
        entry = entry.strip()
        if not entry:
            continue
        entry += '</Car>'
        car = Car.from_xml(entry)
        cars_list.append(car.to_json())

    return cars_list
