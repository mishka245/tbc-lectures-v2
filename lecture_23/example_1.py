
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person({self.name}, {self.age})"


def main():
    p = Person("Giorgi", 44)
    print(p)


if __name__ == "__main__":
    main()
