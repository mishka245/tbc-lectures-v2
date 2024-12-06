import random


class Factory:
    def __init__(self, name):
        self.name = name
        self.cars = []


    def make_car(self):
        print("Making car")
        self.cars.append(f"Car {random.randint(1000, 9999)}")

    def sell_car(self):
        if self.cars:
            print("Sold - ", self.cars.pop(0))
        else:
            raise Exception("Can not sell car")

    def number_of_cars(self):
        return len(self.cars)


    def __str__(self):
        return f"Factory - {self.name}. Produced cars - {self.cars}"


def main():
    f = Factory("GB")

    print(f)
    f.make_car()
    f.make_car()
    print(f)
    f.sell_car()
    print(f)


if __name__ == "__main__":
    main()
