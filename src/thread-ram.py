import threading
import time

import psutil

threads = []
cancel = threading.Event()


def work():
    cancel.wait()


print('threads, resident memory')

for n in range(0, 2001, 100):
    while len(threads) < n:
        t = threading.Thread(target=work)
        t.start()
        threads.append(t)

    time.sleep(2)
    print(f'{n}, {psutil.Process().memory_info().rss}')

cancel.set()
