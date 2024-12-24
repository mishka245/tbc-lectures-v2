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


class Person(Animal):
    def __init__(self, name, age):
        super().__init__(age)
        self.name = name
        self._friends = []

    def get_friends(self):
        [print(friend) for friend in self._friends]

    def add_friend(self, friend):
        if friend is None:
            raise ValueError("Friend cannot be None")
        self._friends.append(friend)

    def speak(self):
        print("hello")

    def age_diff(self, left, right):
        if left.age > right.age:
            print(f"{left.name} is older than {right.name}, by {left.age - right.age} years")
        elif left.age < right.age:
            print(f"{right.name} is older than {left.name}, by {right.age - left.age} years")
        else:
            print(f"{left.name} and {right.name} are of the same age")

    def __str__(self):
        return f"person: {self.name}, {self.age}"



def main():
    person = Person("Alice", 30)
    person.add_friend(Person("Bob", 25))
    person.add_friend(Person("Charlie", 35))
    person.get_friends()
    person.speak()
    person.age_diff(Person("Bob", 25), Person("Charlie", 35))



if __name__ == "__main__":
    main()



