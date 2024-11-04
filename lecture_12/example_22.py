import random


def generate_numbers():
    numbers = []

    for _ in range(20):
        numbers.append(random.randint(1, 1000))
    return numbers


def split_numbers(numbers: list):
    even_numbers = []
    odd_numbers = []

    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)

    return even_numbers, odd_numbers


def display_final_results(numbers, even_numbers, odd_numbers):
    print("Numbers", numbers)
    print("Even numbers", even_numbers)
    print("Odd numbers", odd_numbers)


def main():
    numbers = generate_numbers()
    even_numbers, odd_numbers = split_numbers(numbers)
    display_final_results(numbers, even_numbers, odd_numbers)


if __name__ == "__main__":
    main()
