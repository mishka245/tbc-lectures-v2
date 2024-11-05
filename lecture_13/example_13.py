
def sort_names(names, in_place=False):
    _key = lambda x: x.split(" ")[1]

    if in_place:
        names.sort(key=_key)
        # return None   # ?
        return names  # ?
    return sorted(names, key=_key)


def main():
    my_list = ["giorgi beridze", "john amashukeli",]
    print("Before: ", my_list)
    print("Sorted: ", sort_names(my_list, in_place=True))
    print("After sort: ", my_list)

if __name__ == "__main__":
    main()


