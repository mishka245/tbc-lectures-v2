
def main():
    my_list = [-1, 0, 10, -3, 20]
    my_list_2 = [-10, 1, 3.3, 50]

    result_of_function_map = map(lambda x, y: x * y, my_list, my_list_2)
    # option 1
    print(list(result_of_function_map))
    print(tuple(result_of_function_map))
    print(set(result_of_function_map))
    # option 2
    # for element in result_of_function_map:
    #     print(element)


if __name__ == "__main__":
    main()


