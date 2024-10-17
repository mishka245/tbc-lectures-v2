s = "azcbobobegghakl"

best = ""
test_substring = s[0]
i = 1
while i < len(s):
    if test_substring[-1] <= s[i]:
        test_substring += s[i]
    else:
        if len(test_substring) > len(best):
            best = test_substring
        test_substring = s[i]
    i += 1

print(best)
