import asyncio
from dataclasses import dataclass
from typing import Optional


@dataclass
class ConnectionParams:
    host: str
    port: int


class RdmaConnection:
    """Represents an RDMA connection with asynchronous APIs."""

    def __init__(self, params: ConnectionParams):
        self.params = params
        self.connected = False

    async def connect(self) -> None:
        """Establish the RDMA connection."""
        # In a real implementation, this would perform RDMA handshake logic.
        await asyncio.sleep(0.1)
        self.connected = True

    async def close(self) -> None:
        await asyncio.sleep(0.1)
        self.connected = False

    async def read(self, remote_addr: int, length: int) -> bytes:
        """Read remote memory asynchronously (stub)."""
        await asyncio.sleep(0.1)
        return b"\x00" * length

    async def write(self, remote_addr: int, data: bytes) -> None:
        """Write to remote memory asynchronously (stub)."""
        await asyncio.sleep(0.1)

    async def send(self, data: bytes) -> None:
        """Send a message to the remote endpoint asynchronously (stub)."""
        await asyncio.sleep(0.1)

    async def receive(self) -> bytes:
        """Receive a message from the remote endpoint asynchronously (stub)."""
        await asyncio.sleep(0.1)
        return b""


class RdmaBuilder:
    """Helper for creating RdmaConnection objects."""

    def __init__(self):
        self._host: Optional[str] = None
        self._port: Optional[int] = None

    def with_host(self, host: str) -> "RdmaBuilder":
        self._host = host
        return self

    def with_port(self, port: int) -> "RdmaBuilder":
        self._port = port
        return self

    async def build(self) -> RdmaConnection:
        if self._host is None or self._port is None:
            raise ValueError("Host and port must be specified")
        conn = RdmaConnection(ConnectionParams(self._host, self._port))
        await conn.connect()
        return conn
