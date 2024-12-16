class Person:
    def __init__(self, name, age):
        self.set_name(name)
        self.set_age(age)

    def set_name(self, v):
        self._name = v  # protected attribute

    def get_name(self):
        return self._name

    def set_age(self, v):
        if v < 0:
            raise ValueError("Age can not be negative")
        self._age = v

    def get_age(self):
        return self._age

    def __str__(self):
        return f"Person({self._name}, {self._age})"


def main():
    p = Person("Giorgi", 34)
    # print(p.get_name())
    print(p._name)


if __name__ == "__main__":
    main()
