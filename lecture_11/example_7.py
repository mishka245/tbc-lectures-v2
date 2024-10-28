
def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp-1)


def main():
    print(power(2, 7))


if __name__ == "__main__":
    main()
