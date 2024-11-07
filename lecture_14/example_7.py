def my_func(data: tuple[tuple]) -> tuple[tuple]:
    strings = ()
    numbers = ()
    for inner_tuple in data:
        strings += (inner_tuple[0],)
        numbers += (inner_tuple[1],)

    avg = sum(numbers) / len(numbers)

    return numbers, strings, len(strings), avg


def main():
    my_tuple = (("hi", 5), ("no", 8), ("look", 20), ("hi", 1))
    result = my_func(my_tuple)
    print(result)


if __name__ == "__main__":
    main()
