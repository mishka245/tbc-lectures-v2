fib_counter = 0

def fib(n):
    global fib_counter
    fib_counter = fib_counter + 1
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)

def cached_fib(n, cache):
    # Here we simply count function calls
    global fib_counter
    fib_counter = fib_counter + 1

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
    global fib_counter
    fib(10)
    print("n = 10", f"call count {fib_counter}")
    fib_counter = 0
    fib(15)
    print("n = 15", f"call count {fib_counter}")

    # test cached fib
    print("testing cached fib")
    fib_counter = 0
    cached_fib(10, {})
    print("n = 10", f"call count {fib_counter}")
    fib_counter = 0
    cached_fib(15, {})
    print("n = 15", f"call count {fib_counter}")



if __name__ == "__main__":
    main()



