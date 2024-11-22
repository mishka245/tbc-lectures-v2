
def main():
    data = {"a": ["aardvark"], "b": ["baboon"], "c": ["coati", "cat"], "d": ["donkey", "dog", "dingo"]}

    # result = max(data.items(), key=lambda pair: len(pair[1]))[0]
    for x in data.items():
        print(type(x))
        print(x)



if __name__ == "__main__":
    main()



