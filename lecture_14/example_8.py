

x = None

# case 1 - with == operator
if x == "":  # "" == "" -> True
    print("True")
else:
    print("False")

# case 2 - with automatic bool
if not x:  # not bool(x) -> not bool("") -> not False -> True
    print("True")
else:
    print("False")

