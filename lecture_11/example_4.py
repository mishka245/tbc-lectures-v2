# 3! = 3 * 2 * 1
# n! = n * n-1 * n-2 .... 1

def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)


def main():
    print(fact(5))
    print(fact(0))
    print(fact(10))


if __name__ == "__main__":
    main()