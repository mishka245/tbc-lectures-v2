class Animal:
    def __init__(self, age):
        self.age = age
        self.name = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value

    def __str__(self):
        return f"{self.name} is {self.age} years old"