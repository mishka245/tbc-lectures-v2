

class Human:
    def __init__(self):
        self.__name = None # private attribute

    def set_name(self, v):
        self.__name = v

    def get_name(self):
        return self.__name


    def __str__(self):
        return f"Human({self.__name})"


def main():
    h = Human()
    h.set_name("Giorgi")
    print(h)
    print(h._Human__name)


if __name__ == "__main__":
    main()
