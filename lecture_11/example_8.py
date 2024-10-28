
def power_iter(base, exp):
    result = base
    for _ in range(exp-1):
        result = result * base

    return result


def main():
    print(power_iter(2, 7))


if __name__ == "__main__":
    main()
