
# 2 ^ 4
# 8 * 8 * 8
#

a = 3
final_result = a

exp = 3
exp_counter = 0
while exp_counter < exp - 1:
    result = 0
    i = 0
    while i < a:
        result += final_result
        i += 1
    final_result += result
    exp_counter += 1


print(final_result)
