import time

FILEPATH = "/Users/mikheillomidze/Downloads/googlechrome.dmg"
DATA_COUNT = 100

def load_data():
    for i in range(DATA_COUNT):
        with open(FILEPATH, "rb") as f:
            yield f.read()


def processor(data: list):
    for i,d in enumerate(data):
        print("processing data . . . ", i)
        time.sleep(5)
    print("processing finished")


def main():
    processor(load_data())


if __name__ == "__main__":
    main()
