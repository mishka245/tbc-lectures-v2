
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

def main():
    p1 = Point(3,3)
    p2 = Point(5,10)
    print(str(p1))
    print(p2)


if __name__ == "__main__":
    main()
