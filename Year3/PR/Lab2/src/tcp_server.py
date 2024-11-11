import socket
import threading
import time
import random
import json
from datetime import datetime
import logging
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger(__name__)


class FileManager:
    def __init__(self, filename: str):
        self.filename = filename
        self.read_write_lock = threading.Lock()  # For file access
        self.operation_lock = threading.Lock()  # For operation ordering
        self.active_writers = 0
        self.active_readers = 0
        self.writers_lock = threading.Lock()
        self.readers_lock = threading.Lock()

    def write_message(self, message: Dict):
        """Write message to file with timestamp"""
        with self.writers_lock:
            self.active_writers += 1
            if self.active_writers == 1:
                self.operation_lock.acquire()  # Block readers when writing

        try:
            # Simulate processing time
            sleep_time = random.randint(1, 7)
            logger.info(f"Writing will sleep for {sleep_time} seconds")
            time.sleep(sleep_time)

            with self.read_write_lock:
                try:
                    # Read existing messages
                    messages = []
                    try:
                        with open(self.filename, 'r') as file:
                            messages = json.load(file)
                    except (FileNotFoundError, json.JSONDecodeError):
                        messages = []

                    # Add new message with timestamp
                    message['timestamp'] = datetime.now().isoformat()
                    messages.append(message)

                    # Write back all messages
                    with open(self.filename, 'w') as file:
                        json.dump(messages, file, indent=2)

                    logger.info(f"Written message: {message}")
                    return True
                except Exception as e:
                    logger.error(f"Error writing to file: {e}")
                    return False
        finally:
            with self.writers_lock:
                self.active_writers -= 1
                if self.active_writers == 0:
                    self.operation_lock.release()  # Allow readers when no writers

    def read_messages(self) -> List[Dict]:
        """Read all messages from file"""
        with self.readers_lock:
            # Wait for any write operations to complete
            with self.operation_lock:
                self.active_readers += 1

        try:
            # Simulate processing time
            sleep_time = random.randint(1, 7)
            logger.info(f"Reading will sleep for {sleep_time} seconds")
            time.sleep(sleep_time)

            with self.read_write_lock:
                try:
                    with open(self.filename, 'r') as file:
                        messages = json.load(file)
                        logger.info(f"Read {len(messages)} messages")
                        return messages
                except FileNotFoundError:
                    logger.warning("File not found, returning empty list")
                    return []
                except json.JSONDecodeError:
                    logger.error("Invalid JSON in file, returning empty list")
                    return []
        finally:
            with self.readers_lock:
                self.active_readers -= 1


class TCPServer:
    def __init__(self, host: str, port: int, file_manager: FileManager):
        self.host = host
        self.port = port
        self.file_manager = file_manager
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.running = False

    def start(self):
        """Start the TCP server"""
        self.socket.bind((self.host, self.port))
        self.socket.listen(5)
        self.running = True
        logger.info(f"Server started on {self.host}:{self.port}")

        while self.running:
            try:
                client, address = self.socket.accept()
                logger.info(f"New connection from {address}")
                client_thread = threading.Thread(
                    target=self.handle_client,
                    args=(client, address)
                )
                client_thread.start()
            except Exception as e:
                logger.error(f"Error accepting connection: {e}")

    def handle_client(self, client_socket: socket.socket, address):
        """Handle individual client connections"""
        try:
            while True:
                data = client_socket.recv(1024).decode('utf-8')
                if not data:
                    break

                try:
                    command = json.loads(data)
                    if not isinstance(command, dict) or 'operation' not in command:
                        raise ValueError("Invalid command format")

                    if command['operation'] == 'write':
                        if 'message' not in command:
                            raise ValueError("Write command missing message")

                        # Handle write in a new thread
                        write_thread = threading.Thread(
                            target=self.handle_write,
                            args=(client_socket, command['message'])
                        )
                        write_thread.start()

                    elif command['operation'] == 'read':
                        # Handle read in a new thread
                        read_thread = threading.Thread(
                            target=self.handle_read,
                            args=(client_socket,)
                        )
                        read_thread.start()

                    else:
                        raise ValueError(f"Unknown operation: {command['operation']}")

                except json.JSONDecodeError:
                    logger.error("Invalid JSON received")
                    client_socket.send("Invalid JSON format".encode('utf-8'))
                except ValueError as e:
                    logger.error(f"Invalid command: {e}")
                    client_socket.send(f"Error: {str(e)}".encode('utf-8'))

        except Exception as e:
            logger.error(f"Error handling client {address}: {e}")
        finally:
            client_socket.close()
            logger.info(f"Connection closed for {address}")

    def handle_write(self, client_socket: socket.socket, message: Dict):
        """Handle write operation in separate thread"""
        try:
            success = self.file_manager.write_message(message)
            response = {
                "status": "success" if success else "error",
                "message": "Write operation completed" if success else "Write operation failed"
            }
            client_socket.send(json.dumps(response).encode('utf-8'))
        except Exception as e:
            logger.error(f"Error in write handler: {e}")
            response = {"status": "error", "message": str(e)}
            client_socket.send(json.dumps(response).encode('utf-8'))

    def handle_read(self, client_socket: socket.socket):
        """Handle read operation in separate thread"""
        try:
            messages = self.file_manager.read_messages()
            response = {
                "status": "success",
                "messages": messages
            }
            client_socket.send(json.dumps(response).encode('utf-8'))
        except Exception as e:
            logger.error(f"Error in read handler: {e}")
            response = {"status": "error", "message": str(e)}
            client_socket.send(json.dumps(response).encode('utf-8'))

    def stop(self):
        """Stop the TCP server"""
        self.running = False
        self.socket.close()


def main():
    # Initialize file manager and server
    file_manager = FileManager("messages.json")
    server = TCPServer("0.0.0.0", 5000, file_manager)

    try:
        server.start()
    except KeyboardInterrupt:
        logger.info("Server stopping...")
        server.stop()


if __name__ == "__main__":
    main()
