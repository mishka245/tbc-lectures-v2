
class Animal:
    def __init__(self, species):
        self.species = species

    def speak(self):
        raise NotImplementedError("Abstract function must be implemented by child class")


class CanFly:
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



class Duck(Animal, CanFly, CanSwim):
    def __init__(self):
        super().__init__("Duck")

    def speak(self):
        print("kva kva")


def main():
    d = Duck()
    d.speak()
    print(d.species)



if __name__ == "__main__":
    main()
