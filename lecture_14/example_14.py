def foo():
    for i in range(2):
        print("downloading", i)
        yield i
        print("post download", i)


def main():
    numbers = foo()  # generator
    result_1 = next(numbers)
    print("result_1", result_1)
    result_2 = next(numbers)
    print("result_2", result_2)
    result_3 = next(numbers)




if __name__ == "__main__":
    main()


