def foo():
    for i in range(10):
        print("downloading", i)
        yield i
        print("post download", i)


def main():
    numbers = foo()  # generator
    print(type(numbers))
    print(numbers)
    for number in numbers:
        print("Do some calculation on number", number)


if __name__ == "__main__":
    main()


