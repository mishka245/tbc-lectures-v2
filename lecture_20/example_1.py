from lecture_20.utils import circle_area, circumference


def main():
    radius = int(input("Please enter circle radius - "))
    area = circle_area(radius)
    length = circumference(radius)
    print("Area: ",  area)
    print("Length: ", length)

if __name__ == "__main__":
    main()