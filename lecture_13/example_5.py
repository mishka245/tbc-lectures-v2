from types import FunctionType



def apply_to_each(l: list, f: FunctionType):
    for i in range(len(l)):
        l[i] = f(*l[i])

    return l

def main():
    my_list = [[-1, 0, 10, -3, 20], [-1, 0, 10, -3, 20]]
    apply_to_each(my_list, lambda *args: args[0])
    print(my_list)

if __name__ == "__main__":
    main()


