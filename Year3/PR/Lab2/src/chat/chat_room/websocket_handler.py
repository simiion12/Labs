from fastapi import WebSocket, WebSocketDisconnect


class WebSocketHandler:
    def __init__(self, file_handler):
        self.active_connections: set[WebSocket] = set()
        self.file_handler = file_handler

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.add(websocket)

    async def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            try:
                await connection.send_text(message)
            except:
                await self.disconnect(connection)

    async def handle_client(self, websocket: WebSocket):
        await self.connect(websocket)
        try:
            while True:
                message = await websocket.receive_text()

                if message.startswith("read"):
                    content = await self.file_handler.read_file()
                    await websocket.send_text(f"File content: {content}")
                elif message.startswith("write:"):
                    content = message[6:]  # Remove "write:" prefix
                    await self.file_handler.write_file(content)
                    await self.broadcast(f"New content written: {content}")
                else:
                    await self.broadcast(f"Message: {message}")

        except WebSocketDisconnect:
            await self.disconnect(websocket)