
def dec_to(x, to=2):
    result = ""
    while x != 0:
        result = str(x % to) + result
        x = x // to
    return result

print(dec_to(16))
print(dec_to(16, 2))
print(dec_to(16, 8))
# print(dec_to(16, 16))