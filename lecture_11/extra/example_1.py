import time

def fib(n):
    if n == 1 or n == 0:
        return 1
    return fib(n-1) + fib(n-2)

def fib_user():
    for _ in range(100):
        fib(15)

def main():
    start_time = time.time()  # start
    fib_user()
    end_time = time.time()  # stop
    print("time passed: ", end_time - start_time)


if __name__ == "__main__":
    main()

