
## თუ არსებობს four, არაფერი
## თუ არ არსებობს four, ჩაწერეთ 4

my_dict = {"one": 1, "two": 2, "three": 3, "five": 5, "four": 0}

# if "four" not in my_dict:
#     my_dict["four"] = 4

# my_dict["four"] = my_dict.get("four") or 4
# my_dict["four"] = my_dict.get("four", 4)

if my_dict.get("four") is None:
    my_dict["four"] = 4

print(my_dict)