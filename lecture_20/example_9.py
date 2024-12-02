import random
import time

SEARCH_COUNT = 10000

def get_random_numbers(n=1_000_000):
    for _ in range(n):
        yield random.randint(-100000, 100000)


def search_in(db, value):
    if value in db:
        return True
    return False

def main():
    set_db = set(get_random_numbers())
    list_db = list(set_db)

    search_number = int(input("Please enter number - "))

    start = time.time()
    for i in range(SEARCH_COUNT):
        search_in(list_db, search_number)
    end = time.time()
    print(f"Search in list took - {end-start:.5f}")

    start = time.time()
    for i in range(SEARCH_COUNT):
        search_in(set_db, search_number)
    end = time.time()
    print(f"Search in set took   - {end-start:.5f}")


if __name__ == "__main__":
    main()

