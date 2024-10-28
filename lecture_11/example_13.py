def fib(n):
    if n == 1 or n == 0:
        return 1
    return fib(n-1) + fib(n-2)

def main():
    print(fib(10))
    print(fib(5))
    print(fib(7))
    print(fib(8))
    print(fib(9))


if __name__ == "__main__":
    main()
