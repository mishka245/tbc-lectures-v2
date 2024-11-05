def main():

    my_list = [-1, 0, 10, -3, 20]
    my_list_2 = [-10, 1, 3.3, 50]
    result = list(map(lambda x, y: x * y, my_list, my_list_2))
    # for i in map(lambda x, y: x * y, my_list, my_list_2):
    #     print(i)
    print(result)


if __name__ == "__main__":
    main()


