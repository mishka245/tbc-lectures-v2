
def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)


def main():
    user_input = int(input("please enter positive integer - "))
    print(fact(user_input))


if __name__ == "__main__":
    main()


