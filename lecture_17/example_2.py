
def how_many(d):
    counter = 0
    for v in d.values():
        counter += len(v)

    return counter

def how_many(d):
    lengths = []
    for v in d.values():
        lengths.append(len(v))
    return sum(lengths)


def main():
    data = {"a": ["aardvark"], "b": ["baboon"], "c": ["coati", "cat"], "d": ["donkey", "dog", "dingo"]}

    result = how_many(data)
    print("Total number of animals - ", result)


if __name__ == "__main__":
    main()



