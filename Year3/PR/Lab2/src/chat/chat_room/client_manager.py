from fastapi import WebSocket
import uuid

class ClientManager:
    def __init__(self):
        self.clients = {}

    async def connect(self, websocket: WebSocket):
        # Generate a unique client ID
        client_id = str(uuid.uuid4())

        # Accept the WebSocket connection and add the client
        await websocket.accept()
        self.clients[client_id] = websocket

        print(f"Client {client_id} connected: {len(self.clients)} clients connected")
        return client_id

    async def disconnect(self, client_id):
        # Remove the client from the manager
        websocket = self.clients.pop(client_id)
        await websocket.close()
        print(f"Client {client_id} disconnected: {len(self.clients)} clients connected")

    async def broadcast(self, message):
        # Broadcast the message to all connected clients
        for client_id, websocket in self.clients.items():
            try:
                await websocket.send_text(message)
            except:
                # Remove the client if the WebSocket connection is broken
                await self.disconnect(client_id)

    async def accept_connection(self):
        # Wait for a new client connection
        client_id, websocket = await self.connect(await WebSocket())
        return client_id, websocket