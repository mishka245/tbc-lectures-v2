import dis


def foo():
    print("test")
    l = []
    return None

def bar():
    print("test")
    ll = list()
    return None

dis.dis(foo)
# dis.dis(bar)





