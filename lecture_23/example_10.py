class Person:
    def __init__(self, name, age, height=171):

        # This is mistake
        # self._name = name  # assigne directly to attribute
        # self._age = age  # assigne directly to attribute

        self.name = name  # assigne through property
        self.age = age  # assigne through property
        self.height = height  # assigne through property

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, v):
        self._name = v

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, v):
        if v < 0:
            raise ValueError("Age can not be negative")
        self._age = v

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, v):
        if v < 0:
            raise ValueError("Height can not be negative")
        self.__height = v

    def __str__(self):
        return f"Person({self._name}, {self._age}, {self.__height})"


def main():
    # p = Person("Giorgi", -10)
    p = Person("Giorgi", 44, 184)
    print(p)


if __name__ == "__main__":
    main()
