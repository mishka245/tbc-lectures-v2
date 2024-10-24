
def dec_to(x, to):
    if to > 10:
        raise Exception("Not implemented")
    result = ""
    while x != 0:
        result = str(x % to) + result
        x = x // to
    return result

print(dec_to(16, 10))
print(dec_to(16, 2))
print(dec_to(16, 8))
# print(dec_to(16, 16))