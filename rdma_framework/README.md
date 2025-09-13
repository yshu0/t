# RDMA Framework

This package provides a high-level asynchronous interface for building RDMA
applications. It is intended for educational or prototyping purposes and does
not perform real RDMA operations. Instead, it exposes an API that mimics the
behavior of an RDMA stack so applications can be structured similarly.

## Components

### Connection Establishment

Use `RdmaBuilder` to configure and establish a connection:

```python
from rdma_framework import RdmaBuilder

conn = await RdmaBuilder().with_host("10.0.0.1").with_port(8888).build()
```

`RdmaConnection` exposes async methods `read`, `write`, `send` and `receive` to
interact with the remote endpoint.

### Memory Management

`MemoryManager` manages local and remote memory regions.

* `alloc_local_mr(length)` – allocate a local memory region.
* `request_remote_mr()` – request a remote memory region from the peer.
* `send_mr(mr)` – send a memory region descriptor to the peer.
* `receive_local_mr(addr)` – obtain a local memory region by address.
* `receive_remote_mr()` – receive a remote memory region descriptor.

### Agent and Event Listener

`Agent` executes RDMA requests asynchronously. `EventListener` can register
callbacks and poll for completion events.

```python
from rdma_framework import Agent, EventListener

listener = EventListener()
agent = Agent(listener)

# post a send operation
await agent.post_send(conn.send(b"hello"))

# start the agent and listener loops
asyncio.gather(agent.run(), listener.poll())
```

## Example

See `examples/simple.py` for a basic usage example.
