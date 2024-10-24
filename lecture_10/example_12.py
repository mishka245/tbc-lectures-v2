
def dec_to_bin(x):
    _to = 2
    result = ""
    while x != 0:
        result = str(x % _to) + result
        x = x // _to
    return result

print(dec_to_bin(16))