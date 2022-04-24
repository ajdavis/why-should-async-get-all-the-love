import asyncio

async def do_something():
    await asyncio.sleep(999)

async def main():
    task = asyncio.Task(do_something())
    await asyncio.sleep(1)
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("Task cancelled")

asyncio.run(main())
