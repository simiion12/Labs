import asyncio
import random
from asyncio import Lock


class FileHandler:
    def __init__(self):
        self.file_path = "shared_file.txt"
        self.lock = Lock()
        self.write_count = 0
        self.write_event = asyncio.Event()
        self.write_event.set()  # Initially allow both reads and writes

    async def read_file(self):
        # Wait if there are pending writes
        await self.write_event.wait()

        async with self.lock:
            await asyncio.sleep(random.uniform(1, 7))  # Simulate processing
            try:
                with open(self.file_path, "r") as f:
                    return f.read().strip()
            except FileNotFoundError:
                return ""

    async def write_file(self, content):
        async with self.lock:
            self.write_count += 1
            if self.write_count == 1:
                # First write operation, clear the event to block reads
                self.write_event.clear()

            await asyncio.sleep(random.uniform(1, 7))  # Simulate processing

            try:
                with open(self.file_path, "a") as f:
                    f.write(f"{content}\n")
            finally:
                self.write_count -= 1
                if self.write_count == 0:
                    # Last write operation completed, set the event to allow reads
                    self.write_event.set()