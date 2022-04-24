import threading

counter = 0

def do_something():
    global counter
    print("doing something....")
    counter += 1

t0 = threading.Thread(target=do_something)
t1 = threading.Thread(target=do_something)
t0.start()
t1.start()

lock = threading.Lock()

def do_something():
    global counter
    print("doing something....")
    with lock:
        counter += 1
