import socket
import json
import threading
import time
import random

def send_command(host: str, port: int, command: dict):
    """Send command to TCP server"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.send(json.dumps(command).encode('utf-8'))
        response = s.recv(1024).decode('utf-8')
        print(f"Response: {response}")

def test_concurrent_operations():
    """Test concurrent read and write operations"""
    # Create multiple writer threads
    write_threads = []
    for i in range(5):
        command = {
            "operation": "write",
            "message": {
                "id": i,
                "content": f"Test message {i}",
                "author": f"User {i}"
            }
        }
        thread = threading.Thread(
            target=send_command,
            args=("localhost", 5000, command)
        )
        write_threads.append(thread)

    # Create multiple reader threads
    read_threads = []
    for i in range(3):
        command = {
            "operation": "read"
        }
        thread = threading.Thread(
            target=send_command,
            args=("localhost", 5000, command)
        )
        read_threads.append(thread)

    # Start all threads
    for thread in write_threads + read_threads:
        thread.start()
        # Small delay between thread starts
        time.sleep(random.uniform(0.1, 0.5))

    # Wait for all threads to complete
    for thread in write_threads + read_threads:
        thread.join()

if __name__ == "__main__":
    test_concurrent_operations()
