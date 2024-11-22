def my_func(d):
    return max(d.items(), key=lambda pair: len(pair[1]))[0]

def main():
    data = {"a": ["aardvark"], "b": ["baboon"], "c": ["coati", "cat"], "d": ["donkey", "dog", "dingo"]}

    result = my_func(data)

    print("Maximum length value key is - ", result)


if __name__ == "__main__":
    main()



