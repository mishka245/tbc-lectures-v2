

class Human:
    def __init__(self):
        self.__name = None # private attribute
        self._age = None  # protected attribute

    def set_name(self, v):
        self.__name = v

    def get_name(self):
        return self.__name

    def get_age(self):
        return self._age

    def set_age(self, v):
        self._age = v

    def __str__(self):
        return f"Human({self.__name})"

class Student(Human):

    def __init__(self):
        super().__init__()
        self._email = None

    # seters and getters

    def __str__(self):
        return f"Student({self.get_name()}, {self._age})"


def main():
    h = Human()
    h.set_name("Giorgi")
    print(h._age)  # Do not do like this
    print(h._Human__name)  # Do not do like this


if __name__ == "__main__":
    main()
