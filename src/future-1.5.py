import threading
from concurrent.futures import Future

future0 = Future()
future1 = Future()

def do_something(future):
    global counter
    print("doing something....")
    future.set_result(1)

t0 = threading.Thread(target=do_something, args=(future0,))
t1 = threading.Thread(target=do_something, args=(future1,))
t0.start()
t1.start()
counter = future0.result() + future1.result()
print(f"Counter: {counter}")
