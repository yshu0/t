import asyncio
from dataclasses import dataclass
from typing import Dict, Optional


@dataclass
class MemoryRegion:
    addr: int
    length: int
    data: bytearray


class MemoryManager:
    """Manages local and remote memory regions."""

    def __init__(self):
        self._local_regions: Dict[int, MemoryRegion] = {}
        self._next_addr = 1

    async def alloc_local_mr(self, length: int) -> MemoryRegion:
        await asyncio.sleep(0.05)
        addr = self._next_addr
        self._next_addr += 1
        mr = MemoryRegion(addr=addr, length=length, data=bytearray(length))
        self._local_regions[addr] = mr
        return mr

    async def request_remote_mr(self) -> MemoryRegion:
        await asyncio.sleep(0.05)
        # For demonstration purposes we just create a dummy region
        return MemoryRegion(addr=0xdeadbeef, length=1024, data=bytearray(1024))

    async def send_mr(self, mr: MemoryRegion) -> None:
        await asyncio.sleep(0.05)

    async def receive_local_mr(self, addr: int) -> Optional[MemoryRegion]:
        await asyncio.sleep(0.05)
        return self._local_regions.get(addr)

    async def receive_remote_mr(self) -> MemoryRegion:
        await asyncio.sleep(0.05)
        return MemoryRegion(addr=0xfeedface, length=2048, data=bytearray(2048))
