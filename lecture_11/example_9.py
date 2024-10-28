
# greatest common divisor - gcd
def gcd_iter(a, b):
    m = min(a, b)
    while m > 0:
        if a % m == 0 and b % m == 0:
            return m
        m -= 1

    return m


def main():
    print(gcd_iter(18, 36))
    print(gcd_iter(25, 36))
    print(gcd_iter(21, 36))

if __name__ == "__main__":
    main()
