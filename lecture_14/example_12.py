def foo():
    result = []
    for i in range(10):
        print("downloading", i)
        result.append(i)

    return result

def main():
    numbers = foo()  # type is list
    print(type(numbers))
    for number in numbers:
        print("Do some calculation on number", number)


if __name__ == "__main__":
    main()


