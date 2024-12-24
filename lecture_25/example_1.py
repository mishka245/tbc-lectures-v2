from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Square(Shape):
    def __init__(self, s = 1):
        self.side = s

    def area(self):
        return self.side * self.side

class Circle(Shape):
    def __init__(self, r = 1):
        self.radius = r

    def area(self):
        return 3.14 * self.radius * self.radius



def main():
    # ss1 = Shape()
    s1 = Square(10)
    c1 = Circle(5)
    print(type(s1), s1.area())
    print(type(c1), c1.area())


if __name__ == "__main__":
    main()
