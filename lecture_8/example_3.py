s = "azcbobobegghbob"

# print(s.count("bob"))
search_substring = "bob"
i = 0
counter = 0
l = len(search_substring)
while i <= len(s) - l:
    test_substring = s[i:i+l]
    if test_substring == search_substring:
        counter += 1
    i += 1

print(counter)