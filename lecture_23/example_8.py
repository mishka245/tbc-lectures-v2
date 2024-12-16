class Person:
    def __init__(self, name, age):
        self._name = None
        self._age = None
        self.set_name(name)
        self.set_age(age)

    def set_name(self, v):
        self._name = v

    def get_name(self):
        return self._name

    def set_age(self, v):
        if v < 0:
            raise ValueError("Age can not be negative")
        self._age = v

    def get_age(self):
        return self._age

    def __foo(self):
        pass

    def __str__(self):
        return f"Person({self._name}, {self._age})"


def main():
    p = Person("Giorgi", 44)
    p.set_name("Nini")
    p.set_age(34)
    print(p.get_name())
    print(p.get_age())


if __name__ == "__main__":
    main()
