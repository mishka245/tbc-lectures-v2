def multiply(a, b):
    result = 0
    for _ in range(b):
        result = result + a
    return result

def power(base, exp):
    result = base
    for _ in range(1, exp):
        result = multiply(result, base)
    return result

base = 2
exp = 3
print(f"{base}^{exp} = {power(base, exp)}")




