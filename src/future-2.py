from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor()

def do_something():
    print("doing something....")
    return 1

future0 = executor.submit(do_something)
future1 = executor.submit(do_something)
counter = future0.result() + future1.result()
print(f"Counter: {counter}")
