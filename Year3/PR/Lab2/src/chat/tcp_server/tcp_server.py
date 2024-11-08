import asyncio
from .message_handler import MessageHandler
import random
import time

class TCPServer:
    def __init__(self):
        self.message_handler = MessageHandler()

    async def handle_client(self, reader, writer):
        print("New TCP client connected")
        try:
            while True:
                data = await reader.read(1024)
                if not data:
                    break
                message = data.decode().strip()
                print(f"Received message: {message}")
                # Process the message
                await self.message_handler.handle_message(message)
                # Simulate some processing time
                await asyncio.sleep(random.uniform(1, 7))
                # Send a response back to the client
                response = f"Server response: {message}"
                writer.write(response.encode())
                await writer.drain()
        finally:
            print("Client disconnected")
            writer.close()
            await writer.wait_closed()

    async def run(self):
        print("TCP server running...")
        server = await asyncio.start_server(self.handle_client, "127.0.0.1", 8000)
        async with server:
            await server.serve_forever()