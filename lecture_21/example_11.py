import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) **2)


def main():
    p1 = Point(3,3)
    p2 = Point(5,10)
    print(str(p1))
    print(p2)
    print(p1.distance(p2))
    print(p2.distance(p1))


if __name__ == "__main__":
    main()
