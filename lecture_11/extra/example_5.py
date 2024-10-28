import timeit



def fib(n=20):
    if n == 1 or n == 0:
        return 1
    return fib(n-1) + fib(n-2)

def fib_iter(n=20):
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

def main():
    result = timeit.timeit(fib, number=1000)
    print("time passed: ", result)

    result = timeit.timeit(fib_iter, number=1000)
    print("time passed iter: ", result)


if __name__ == "__main__":
    main()

