from contextlib import contextmanager


@contextmanager
def foo():
    print("Enter foo")
    yield
    print("Exit foo")


# custom decorator
def my_decorator(f):
    def wrapper(*args, **kwargs):
        print("Enter", f.__name__)
        f(*args, **kwargs)
        print("Exit", f.__name__)
    return wrapper

@my_decorator
def bar():
    print("Inside bar")

# decorator with arguments example
def my_decorator_with_args(arg):
    def inner_decorator(f):
        def wrapper(*args, **kwargs):
            print("Enter", f.__name__, arg)
            f(*args, **kwargs)
            print("Exit", f.__name__, arg)
        return wrapper
    return inner_decorator