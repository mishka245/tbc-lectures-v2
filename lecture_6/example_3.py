
# 2 ^ 4
# 2 * 2 * 2 * 2
#

result = 0
exp = 3
base = 2
i = 0
while i < exp :
    temp_result = 0
    temp_i = 0
    while temp_i < base:
        temp_result += base
        temp_i += 1

    result += temp_result
    # print(result)
    i += 1

print(result)

