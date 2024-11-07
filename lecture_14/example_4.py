import random


# generate 20 random number
# split numbers into two different tuples
def generate_random_numbers(n:int) -> tuple:
    t = tuple()

    for i in range(n):
        t = t + (random.randint(10, 100),)

    return t


def split_numbers(numbers: tuple[int]) -> tuple[tuple[int], tuple[int]]:
    evens = []
    odds = []
    for number in numbers:
        if number % 2 == 0:
            evens.append(number)
        else:
            odds.append(number)

    return tuple(evens), tuple(odds)



def main():
    numbers = generate_random_numbers(20)
    evens, odds = split_numbers(numbers)
    print(numbers)
    print(evens)
    print(odds)


if __name__ == "__main__":
    main()
