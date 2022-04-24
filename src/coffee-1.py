import time
from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor()


def heat_water():
    ...

def grind_coffee():
    ...

def brew(future1, future2):
    future1.result()
    future2.result()
    time.sleep(4 * 60)  # Brew for 4 minutes.

heated_future = executor.submit(heat_water)
ground_future = executor.submit(grind_coffee)
brew(heated_future, ground_future)
print("Drinking coffee")
