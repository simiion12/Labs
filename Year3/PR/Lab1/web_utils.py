import ssl
import socket
from urllib.parse import urlparse


def get_webpage(url, max_redirects=5):
    for _ in range(max_redirects):
        parsed_url = urlparse(url)
        host = parsed_url.netloc
        path = parsed_url.path if parsed_url.path else '/'
        port = 443 if parsed_url.scheme == 'https' else 80  # Ensure port is always an integer

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
            # This is a redirect
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
