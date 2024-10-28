def mult(a, b):
    result = 0
    for _ in range(b):  # 0 + 5 + 5 + 5 + 5 + 5 + 5 + 5
        result += a

    return result


def main():
    print(mult(5, 7))


if __name__ == "__main__":
    main()
