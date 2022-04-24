import asyncio

async def call_some_coroutine():
    pass

counter = 0

async def do_something():
    global counter
    print("doing something....")
    await call_some_coroutine()
    counter += 1

async def main():
    t0 = asyncio.Task(do_something())
    t1 = asyncio.Task(do_something())
    await asyncio.gather(t0, t1)
    print(counter)

asyncio.run(main())
