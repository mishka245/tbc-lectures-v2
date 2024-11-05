
def sort_names(names):
    return sorted(names, key=lambda x: x.split(" ")[1])


def main():
    my_list = ["giorgi beridze", "john amashukeli",]
    print("Before: ", my_list)
    print("Sorted: ", sort_names(my_list))
    print("After sort: ", my_list)

if __name__ == "__main__":
    main()


