def main():
    data = {"a": ["aardvark"], "b": ["baboon"], "c": ["coati", "cat"], "d": ["donkey", "dog", "dingo"]}

    result = sum((len(v) for v in data.values()))
    print("Total number of animals - ", result)


if __name__ == "__main__":
    main()



