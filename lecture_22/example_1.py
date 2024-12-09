# მემკვიდრეობა
# პოლიმორფიზმი
# ენკაფსულაცია
# აბსტრაქცია



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
    a = Animal("Dino", 10000000)
    c.say_hello()
    a.say_hello()

    print(a)
    print(c)


if __name__ == "__main__":
    main()

