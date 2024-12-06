import random


class MyList:
    number_of_elements = 20
    def __init__(self):
        self.data = []

    def fill(self):
        for _ in range(self.number_of_elements):
            self.data.append(random.randint(-100, 200))

    def average(self):
        return sum(self.data) / self.number_of_elements

    def odd(self):
        result = []
        for element in self.data:
            if element % 2 != 0:
                result.append(element)
        return result

    def even(self):
        return [x for x in self.data if x % 2 == 0]

def main():
    l = MyList()
    l.fill()
    print(l.average())
    print(l.odd())
    print(l.even())


if __name__ == "__main__":
    main()
