
class Animal:
    def __init__(self, species):
        self.species = species

    def speak(self):
        raise NotImplementedError("Abstract function must be implemented by child class")

    def fly(self):
        pass


class Rabit(Animal):
    pass

class Bird(Animal):
    pass


class Duck(Animal):
    pass

    def swim(self):
        pass

