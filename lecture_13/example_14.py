# order list of lists with third element
def main():
    my_list = [[1, 2, 3], [2, 2, 2], [100, 10, 200], [-1, 0, -2]]
    print("Sorted: ", sorted(my_list, key=lambda l: l[2], reverse=True))


if __name__ == "__main__":
    main()
