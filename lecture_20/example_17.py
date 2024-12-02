import random


def generate_random_numbers() -> set:
    result = set()
    while len(result) < 50:
        rand_number = random.randint(10, 1000)
        if rand_number not in result:
            result.add(rand_number)

    return result

def main():
    print(generate_random_numbers())


if __name__ == "__main__":
    main()
