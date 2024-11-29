
def foo():
    pass

def update_db():
    try:
        print("Connecting to db . . .")
        print("Connected.")
        raise  BaseException
        a = "3"
        b = "1"
        a = int(a)
        b = int(b)
        result = a / b
        print(f"Writing {result} in DB")
        print(f"Writing in another db {100 + str(result)}")
    except ValueError as e:
        print("can not convert into numbers")
    except ZeroDivisionError as e:
        print("Can not divide by 0")
    except Exception as ex:
        print("Unknown exception occurred", ex)
    finally:
        foo()
        print("Closing db connection . . .")
        print("Closed.")

def main():
    update_db()


if __name__ == "__main__":
    main()




