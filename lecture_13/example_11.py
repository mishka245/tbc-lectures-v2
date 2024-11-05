def main():
    my_list = [-1, 0, 10, -3, 20]
    my_list_2 = [-10, 1, 3.3, 50]
    # for i in map(lambda a, b: (a + b) / 2, my_list, my_list_2):
    #     print(i)
    print(list(map(lambda a, b: (a + b) / 2, my_list, my_list_2)))

if __name__ == "__main__":
    main()


