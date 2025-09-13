import asyncio
from typing import Callable, Awaitable


class EventListener:
    """Listens for RDMA completion events."""

    def __init__(self):
        self._callbacks = []

    def register(self, callback: Callable[[], Awaitable[None]]) -> None:
        self._callbacks.append(callback)

    async def poll(self) -> None:
        """Poll for completion events and invoke callbacks."""
        while True:
            await asyncio.sleep(0.1)
            for cb in list(self._callbacks):
                await cb()


class Agent:
    """Executes RDMA requests asynchronously."""

    def __init__(self, listener: EventListener):
        self.listener = listener
        self._queue = asyncio.Queue()

    async def post_send(self, coro: Awaitable[None]) -> None:
        await self._queue.put(coro)

    async def run(self) -> None:
        while True:
            coro = await self._queue.get()
            await coro
            self._queue.task_done()
