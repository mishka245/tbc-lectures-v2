
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello, my name is - {self.name}")

    def __str__(self):
        return f"Animal: {self.name}, Age {self.age}"


class Cat(Animal):

    def __str__(self):
        return f"Cat: {self.name}, Age {self.age}"


def main():
    c = Cat("Fiso", 1)
    a = Animal("test", 111)
    print("isinstance(c, Cat)", isinstance(c, Cat))
    print("isinstance(c, Animal)", isinstance(c, Animal))
    print("isinstance(c, object)", isinstance(c, object))
    print("isinstance(a, object)", isinstance(a, object))
    print("isinstance(a, Cat)", isinstance(a, Cat))
    print(type(c), type(a))
    c.say_hello()
    a.say_hello()


if __name__ == "__main__":
    main()

