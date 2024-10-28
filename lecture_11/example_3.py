def mult(a, b):
    if b > 0:
        return a + mult(a, b-1)
    else:
        return 0


def main():
    print(mult(5, 3))
#      mult(5, 3)
#      5 + mult(5, 2)
#      5 + 5 + mult(5, 1)
#      5 + 5 + 5 + mult(5, 0)
#      5 + 5 + 5 + 0

if __name__ == "__main__":
    main()
