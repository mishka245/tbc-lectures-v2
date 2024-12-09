
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello, my name is - {self.name}")

    def __str__(self):
        return f"Animal: {self.name}, Age {self.age}"

class Chicken(Animal):
    def __init__(self, name, age, legs):
        # self.name = name
        # self.age = age
        super().__init__(name, age)

        self.legs = legs

    def print_legs(self):
        print(self.legs)


def main():
    c = Chicken("Ricky",4, 2)

if __name__ == "__main__":
    main()

