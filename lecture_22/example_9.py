
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __add__(self, other: "Point"):
        if not isinstance(other, Point):
            raise TypeError(f"+ operator is not defined for Point and {type(other)}")
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __eq__(self, other: "Point"):
        return self.x == other.x and self.y == other.y


def main():
    p1 = Point(1,1)
    p2 = Point(2,4)
    # p3 = p1 + 20
    p3 = 20 + p1
    print(p3)


if __name__ == "__main__":
    main()
