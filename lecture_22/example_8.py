
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __add__(self, other: "Point"):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __eq__(self, other: "Point"):
        return self.x == other.x and self.y == other.y




def main():
    p1 = Point(1,1)
    p2 = Point(2,4)
    p3 = p1 + p2
    print(p3)

    # if p1 == p2 ?
    # if p1.x == p2.x and p1.y == p2.y:
    #     pass
    if p1 == p2:
        print("p1 == p2")
    else:
        print("p1 != p2")

    if Point(0, 1) == Point(0, 1):
        print("Point(0, 1) == Point(0, 1)")
    else:
        print("Point(0, 1) != Point(0, 1)")



if __name__ == "__main__":
    main()
