def mult_rec(a, b):
    if b > 0:
        return a + mult_rec(a, b-1)
    else:
        return 0

def mult_iter(a, b):
    result = 0
    for _ in range(b):
        result += a

    return result



def main():
    print(mult_iter(100, 100))
    print(mult_rec(100, 100))

    print(mult_iter(1000, 1000))
    print(mult_rec(1000, 1000))


if __name__ == "__main__":
    main()
