
def whoala(i,  j) -> int:

    assert j != 0, "wrong number. can not divide on 0"

    return i / j

def foo(t, c):
    return whoala(t, c)

def bar(a ,b):
    foo(a, b)
    return "test"

def main():

    try:
        print(bar(1, 0))
    except (ValueError, ZeroDivisionError) as ex:
        print("Wow, I called function with wrong arguments. Have to think something better", ex)


if __name__ == "__main__":
    main()
