


def get_max_value_len_key(d):
    max_len = -1
    max_key = None
    for k, v in d.items():
        if len(v) > max_len:
            max_len = len(v)
            max_key = k

    return max_key

def main():
    data = {"a": ["aardvark"], "b": ["baboon"], "c": ["coati", "cat"], "d": ["donkey", "dog", "dingo"]}

    result = get_max_value_len_key(data)
    print("Maximum length value key is - ", result)


if __name__ == "__main__":
    main()



