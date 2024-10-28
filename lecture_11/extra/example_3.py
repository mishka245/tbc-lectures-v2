import time

def fib(n):
    if n == 1 or n == 0:
        return 1
    return fib(n-1) + fib(n-2)

def fib_iter(n):
    a = 0
    b = 1
    c = 0
    counter = 0
    while counter < n:
        c = a + b
        a = b
        b = c
        counter += 1
    return c

def fib_user():
    for _ in range(10000):
        fib(15)

def fib_user_iter():
    for _ in range(10000):
        fib_iter(15)

def main():
    start_time = time.time()  # start
    fib_user()
    end_time = time.time()  # stop
    print("time passed (recursive): ", end_time - start_time)
    start_time = time.time()  # start
    fib_user_iter()
    end_time = time.time()  # stop
    print("time passed (iteration): ", end_time - start_time)



if __name__ == "__main__":
    main()

