

# Do not do at home :D
class int(int):

    def __add__(self, other):
        return self * other


def main():
    print(int(2) + int(2))
    print(int(2) + int(3))
    print(2 + 3)




if __name__ == "__main__":
    main()
