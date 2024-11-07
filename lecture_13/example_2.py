from types import FunctionType


def multiply_on_10(x):
    return x * 10

def apply_to_each(l: list, f: FunctionType):
    for i in range(len(l)):
        l[i] = f(l[i])

    return l

def main():
    my_list = [-1, 0, 10, -3, 20]
    result = apply_to_each(my_list, multiply_on_10)

    print(result)

if __name__ == "__main__":
    main()

