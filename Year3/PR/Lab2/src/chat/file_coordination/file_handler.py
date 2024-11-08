from .synchronization import Mutex
import random
import time
import asyncio

class FileHandler:
    def __init__(self):
        self.mutex = Mutex()
        self.file_path = "shared_file.txt"

    async def read_file(self):
        # Acquire the mutex manually
        await self.mutex.acquire()
        try:
            with open(self.file_path, "r") as file:
                data = file.read().strip()
            # Simulate some processing time
            await asyncio.sleep(random.uniform(1, 7))
            return data
        finally:
            # Release the mutex
            await self.mutex.release()

    async def write_file(self, data):
        # Acquire the mutex manually
        await self.mutex.acquire()
        try:
            with open(self.file_path, "a") as file:
                file.write(f"{data}\n")
            # Simulate some processing time
            await asyncio.sleep(random.uniform(1, 7))
        finally:
            # Release the mutex
            await self.mutex.release()
