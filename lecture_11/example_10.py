
# greatest common divisor - gcd
def gcd_rec(a, b):
    if b == 0:
        return a
    return gcd_rec(a, b%a)



def main():
    print(gcd_rec(18, 36))
    print(gcd_rec(25, 36))
    print(gcd_rec(21, 36))

if __name__ == "__main__":
    main()
