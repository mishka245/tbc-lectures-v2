def safe_divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Err"


def main():
    a = [1, 2, 3, 4, 5, 600, 123]
    b = [1, 200, 3, 0, 5, 6]
    result = [safe_divide(x,y) for x, y in zip(a, b)]
    print(result)


if __name__ == "__main__":
    main()
