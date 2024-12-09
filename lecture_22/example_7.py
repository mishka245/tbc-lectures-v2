
class Animal:
    def __init__(self, species):
        self.species = species

    def speak(self):
        raise NotImplementedError("Abstract function must be implemented by child class")


class CanFly:
    def __init__(self, speed):
        self.speed = speed

    def fly(self):
        pass

class CanSwim:
    def swim(self):
        pass

class Rabit(Animal):
    pass

class Bird(Animal, CanFly):
    def __init__(self):
        super().__init__("Bird")

class Foo:
    pass

class Duck(Animal, CanFly, CanSwim, Foo):
    def __init__(self, speed):
        CanFly.__init__(self, speed)
        super().__init__("Duck")

    def speak(self):
        print("kva kva")


def main():
    d = Duck(35)
    d.speak()
    print(d.species)
    print(d.speed)



if __name__ == "__main__":
    main()
