l = [10, 10,1, 2, 3, 4, 4, 4, 5, 5]

seen = set()
result = []
for number in l:
    if number not in seen:
        result.append(number)
        seen.add(number)

print(result)