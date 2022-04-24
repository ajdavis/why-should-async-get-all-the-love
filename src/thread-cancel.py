import time
from concurrent.futures import ThreadPoolExecutor

class ThreadCancelledError(BaseException):
    pass

class CancellationToken:
    is_cancelled = False

    def check_cancelled(self):
        if self.is_cancelled:
            raise ThreadCancelledError()

def do_something(token):
    while True:
        token.check_cancelled()

token = CancellationToken()
executor = ThreadPoolExecutor()
future = executor.submit(do_something, token)
time.sleep(1)
token.is_cancelled = True
try:
    # Wait for do_something to notice that it's cancelled.
    future.result()
except ThreadCancelledError:
    print("Thread cancelled")
