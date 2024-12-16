
def pseudo_calculation():
    return -27


class Person:
    def __init__(self, name, age):
        self.set_name(name)
        self.set_age(age)

    def set_name(self, v):
        self.name = v

    def get_name(self):
        return self.name

    def set_age(self, v):
        if v < 0:
            raise ValueError("Age can not be negative")
        self.age = v

    def get_age(self):
        return self.age

    def __str__(self):
        return f"Person({self.name}, {self.age})"


def main():

    p = Person("Giorgi", pseudo_calculation())
    print(p)


if __name__ == "__main__":
    main()
