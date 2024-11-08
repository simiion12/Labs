import asyncio

class Mutex:
    def __init__(self):
        self.lock = asyncio.Lock()

    async def acquire(self):
        await self.lock.acquire()

    async def release(self):
        self.lock.release()