
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_coordinates(self):
        print(self.x, self.y)

def main():
    p1 = Point(3,3)
    p2 = Point(5,10)
    print(p1)
    print(p2)
    p1.print_coordinates()
    p2.print_coordinates()


if __name__ == "__main__":
    main()
