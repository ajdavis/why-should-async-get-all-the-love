import time
from concurrent.futures import ThreadPoolExecutor, as_completed

executor = ThreadPoolExecutor()

def heat_water():
    return "heated water"

def grind_coffee():
    return "ground coffee"

def brew(future1, future2):
    for future in as_completed([future1, future2]):
        print(f"Adding {future.result()} to French press")
    time.sleep(4 * 60)  # Brew for 4 minutes.

heated_future = executor.submit(heat_water)
ground_future = executor.submit(grind_coffee)
brew(heated_future, ground_future)
print("Drinking coffee")
