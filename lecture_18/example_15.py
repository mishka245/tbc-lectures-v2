import time
from contextlib import contextmanager


@contextmanager
def timer():
    # Setup
    start = time.time()

    yield  # context manager body works here

    # cleanup
    end = time.time()
    print(f"Time elapsed - {end - start:.4f} seconds")


with timer() as list_from_contextmanager:
    for _ in range(100000000):
        pass



