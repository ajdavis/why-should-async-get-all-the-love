import asyncio

import psutil

tasks = []


async def work():
    while True:
        await asyncio.sleep(100)


async def main():
    print('tasks, resident memory')

    for n in range(0, 2001, 100):
        while len(tasks) < n:
            t = asyncio.create_task(work())
            tasks.append(t)

        await asyncio.sleep(2)
        print(f'{n}, {psutil.Process().memory_info().rss}')


asyncio.run(main())
