import asyncio
import random


class TCPServer:
    def __init__(self, file_handler, websocket_handler=None):
        self.file_handler = file_handler
        self.websocket_handler = websocket_handler  # Add WebSocket handler reference

    async def handle_client(self, reader, writer):
        try:
            while True:
                data = await reader.read(1024)
                if not data:
                    break

                message = data.decode().strip()
                print(f"TCP Server received: {message}")

                # Process commands
                if message.startswith("read"):
                    content = await self.file_handler.read_file()
                    response = f"File content: {content}"
                    # Broadcast to WebSocket clients
                    if self.websocket_handler:
                        await self.websocket_handler.broadcast(f"TCP Client read file: {content}")
                elif message.startswith("write:"):
                    content = message[6:]  # Remove "write:" prefix
                    await self.file_handler.write_file(content)
                    response = f"Written to file: {content}"
                    # Broadcast to WebSocket clients
                    if self.websocket_handler:
                        await self.websocket_handler.broadcast(f"TCP Client wrote to file: {content}")
                else:
                    response = "Invalid command"
                    if self.websocket_handler:
                        await self.websocket_handler.broadcast(f"TCP Client sent: {message}")

                writer.write(response.encode())
                await writer.drain()

        except Exception as e:
            print(f"Error handling TCP client: {e}")
        finally:
            writer.close()
            await writer.wait_closed()

    async def run(self):
        server = await asyncio.start_server(
            self.handle_client, '0.0.0.0', 8001
        )
        print("TCP server running on port 8001")
        async with server:
            await server.serve_forever()
