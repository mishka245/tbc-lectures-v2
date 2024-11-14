my_dict = {"one": 1, "two": 2, "three": 3, "five": 5}

may_be_existing_value_or_default = my_dict.get("four") or 4
my_dict["four"] = my_dict

print(my_dict)