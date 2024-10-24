x = 5


def f():
    global x
    x = x + 1
    print(x)


f()

print(x)

