import time

ITERATIONS_COUNT = 50

def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)

def cached_fib(n, cache={}):
    # if cache is None:
    #     cache = {}
    if val := cache.get(n):
        return val
    if n == 1 or n == 2:
        result = 1
    else:
        result = cached_fib(n-1, cache) + cached_fib(n-2, cache)
    cache[n] = result

    return result


def measure_func(func):
    start = time.time()
    for _ in range(ITERATIONS_COUNT):
        func(35)
    end = time.time()
    return end - start


def main():
    print("time for non cached version", measure_func(fib))


    print("time for cached version", measure_func(cached_fib))



if __name__ == "__main__":
    main()



