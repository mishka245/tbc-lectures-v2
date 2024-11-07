def foo(a, *, c):   # forcing key-word only argument c
    print(a, c)

def bar(a, *args, c):
    print("a", a)
    print("args", args)
    print("c", c)

def tor(a, b, *args):
    print(a, b)

foo(1, c=2)
foo(1, c=2)
bar(1, 2,3, c=2)
bar(1, 2,3, c=3)

print("testing tor")
# tor(1)
tor(1, 2)
tor(1, 2, 3)
