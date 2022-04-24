from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor()

def do_something(_):
    print("doing something....")
    return 1

counter = sum(executor.map(do_something, range(2)))
print(f"Counter: {counter}")
