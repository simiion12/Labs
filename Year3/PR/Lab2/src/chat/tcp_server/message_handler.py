from ..file_coordination.file_handler import FileHandler
import random
import time

class MessageHandler:
    def __init__(self):
        self.file_handler = FileHandler()

    async def handle_message(self, message):
        # Parse the message to determine if it's a read or write operation
        if message.startswith("read"):
            await self.handle_read_operation()
        elif message.startswith("write"):
            data = message.split(":")[1].strip()
            await self.handle_write_operation(data)
        else:
            print(f"Unknown message: {message}")

    async def handle_read_operation(self):
        async with self.file_handler.mutex:
            # Read from the shared file
            data = await self.file_handler.read_file()
            print(f"Read operation: {data}")

    async def handle_write_operation(self, data):
        async with self.file_handler.mutex:
            # Write to the shared file
            await self.file_handler.write_file(data)
            print(f"Write operation: {data}")