counter = 0


def cached_fib(n, cache):
    # Here we simply count function calls
    global counter
    counter = counter + 1

    # Here we check if fibnaoci number is already calculated for n
    if cache.get(n):
        return cache.get(n)

    # fibonaci number calculation
    if n == 1 or n == 2:
        result = 1
    else:
        result = cached_fib(n-1, cache) + cached_fib(n-2, cache)

    # Cache calculated number
    cache[n] = result

    return result

def main():
    global counter
    # test cached fib
    cache = {}
    print("testing cached fib")
    counter = 0
    cached_fib(10, cache)
    print("n = 10", f"call count {counter}")
    counter = 0
    cached_fib(15, cache)
    print("n = 15", f"call count {counter}")



if __name__ == "__main__":
    main()



