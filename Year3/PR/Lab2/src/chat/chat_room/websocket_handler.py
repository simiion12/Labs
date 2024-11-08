from fastapi import WebSocket, WebSocketDisconnect
from ..file_coordination.file_handler import FileHandler
import asyncio

class WebSocketHandler:
    def __init__(self):
        self.clients = set()
        self.file_handler = FileHandler()

    async def handle_client(self, websocket: WebSocket):
        # Add the new client to the set of connected clients
        self.clients.add(websocket)
        await websocket.accept()

        try:
            async for message in websocket.iter_text():
                if message.startswith("read"):
                    data = await self.file_handler.read_file()
                    await websocket.send_text(f"File content: {data}")
                elif message.startswith("write"):
                    data = message.split(":")[1].strip()
                    await self.file_handler.write_file(data)
                    await websocket.send_text(f"Wrote '{data}' to the file.")
                else:
                    # Broadcast the message to all connected clients
                    await self.broadcast(message)
        except WebSocketDisconnect:
            # Remove the client from the set when they disconnect
            self.clients.remove(websocket)

    async def broadcast(self, message):
        # Send the message to all connected clients
        for client in self.clients:
            try:
                await client.send_text(message)
            except:
                # Remove the client if the WebSocket connection is broken
                self.clients.remove(client)

    async def run(self):
        print("WebSocket handler running...")
        while True:
            # Wait for a new client connection
            client, websocket = await self.accept_connection()
            asyncio.create_task(self.handle_client(websocket))

    async def accept_connection(self):
        # Wait for a new client connection
        websocket = await WebSocket()
        return websocket, websocket