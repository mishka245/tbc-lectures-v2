from types import FunctionType



def apply_to_each(l: list, f: FunctionType):
    for i in range(len(l)):
        l[i] = f(l[i])

    return l

def main():
    my_list = [-1, 0, 10, -3, 20]
    result = apply_to_each(my_list, lambda x: x * 10)
    print(result)
    result_2 = apply_to_each(my_list, lambda x: x ** 2)

    print(result_2)

if __name__ == "__main__":
    main()


