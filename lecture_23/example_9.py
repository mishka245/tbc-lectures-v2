class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

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

    def __str__(self):
        return f"Person({self._name}, {self._age})"


def main():
    p = Person("Giorgi", 44)
    p.name = "Nini"
    try:
        p.age = -34
    except Exception as ex:
        print("Could not assigne negative value", ex)

    print(p.name)
    print(p.age)


if __name__ == "__main__":
    main()
