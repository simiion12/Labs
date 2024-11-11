from fastapi.websockets import WebSocket
from typing import Dict, Set
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ChatRoom:
    def __init__(self):
        self.active_connections: Dict[str, WebSocket] = {}
        self.messages: list = []

    async def connect(self, websocket: WebSocket, client_id: str):
        await websocket.accept()
        self.active_connections[client_id] = websocket
        await self.broadcast(f"Client {client_id} joined the chat")

    def disconnect(self, client_id: str):
        if client_id in self.active_connections:
            del self.active_connections[client_id]

    async def broadcast(self, message: str):
        self.messages.append(message)
        for connection in self.active_connections.values():
            try:
                await connection.send_text(message)
            except Exception as e:
                logger.error(f"Error broadcasting message: {e}")

    def get_active_clients(self) -> Set[str]:
        return set(self.active_connections.keys())
