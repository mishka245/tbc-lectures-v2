def foo(n: int) -> int:
    return n ** 2

def bar(n: int) -> int:
    return f"{n} - {n}"

def main():
    print(foo(2))
    print(bar("test"))


if __name__ == "__main__":
    main()
