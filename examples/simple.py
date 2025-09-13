import asyncio
from rdma_framework import RdmaBuilder, MemoryManager, Agent, EventListener


async def main():
    conn = await RdmaBuilder().with_host("localhost").with_port(9999).build()
    mem = MemoryManager()
    mr = await mem.alloc_local_mr(128)

    listener = EventListener()
    agent = Agent(listener)

    await agent.post_send(conn.send(b"hello"))

    # run agent and listener concurrently for one iteration
    await asyncio.gather(agent.run(), listener.poll())


if __name__ == "__main__":
    asyncio.run(main())
