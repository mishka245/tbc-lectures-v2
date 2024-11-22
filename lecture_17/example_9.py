

def cached_fib(n, cache, *, counter = 0):
    # Here we check if fibnaoci number is already calculated for n
    if cache.get(n):
        return cache.get(n)

    # fibonaci number calculation
    if n == 1 or n == 2:
        result = 1
        counter = 1
    else:
        fib_n_1_pair =  cached_fib(n-1, cache, counter=counter)
        fib_n_2_pair =  cached_fib(n-2, cache, counter=counter)
        counter = fib_n_1_pair[1] +  fib_n_2_pair[1]
        result = fib_n_1_pair[0] +  fib_n_2_pair[0]

    counter = counter + 1
    # Cache calculated number
    cache[n] = (result, counter)

    return result, counter

def main():
    # test cached fib
    cache = {}
    print("testing cached fib")
    _, counter = cached_fib(10, cache)
    print("n = 10", f"call count {counter}")
    _, counter = cached_fib(15, cache)
    print("n = 15", f"call count {counter}")



if __name__ == "__main__":
    main()



