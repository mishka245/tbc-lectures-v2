from typing import List


class Shape:
    def area(self):
        # raise NotImplementedError("Subclasses must implement this method")
        return -1

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

class Hexagon(Shape):
    def __init__(self, s = 1):
        self.side = s

def print_areas(s: List[Shape]):
    for shape in s:
        print(type(shape), "Area - ", shape.area())


def main():
    s1 = Square(10)
    c1 = Circle(5)
    s2 = Square(20)
    c2 = Circle(10)
    h1 = Hexagon(5)
    shapes = [s1, c1, s2, c2, h1]
    print_areas(shapes)


if __name__ == "__main__":
    main()
