def power(base, exp):
    result = base
    for _ in range(1, exp):
        # multiply result on base
        m = 0
        for _ in range(base):
            m = m + result
        # save new value into result
        result = m
    return result

base = 2
exp = 7
print(f"{base}^{exp} = {power(base, exp)}")




