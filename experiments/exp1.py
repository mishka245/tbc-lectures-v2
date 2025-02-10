import random

def main():
    results = {
        "x and y are both less than 4": 0,
        "x and y are both greater than 6": 0,
        "x is between 4 and 6": 0,
        "y is not equal to 5": 0,
        "None of the conditions are met": 0,
    }

    for i in range(1000000):
        x = random.randint(0, 9)  # rand.Intn(10) generates a random number between 0 and 9
        y = random.randint(0, 9)
        print(f"Iteration {i} \tx: {x}, y: {y} \t", end="")

        if x < 4 and y < 4:
            print("x and y are both less than 4")
            results["x and y are both less than 4"] += 1
        elif x > 6 and y > 6:
            print("x and y are both greater than 6")
            results["x and y are both greater than 6"] += 1
        elif 4 <= x <= 6:
            print("x is between 4 and 6")
            results["x is between 4 and 6"] += 1
        elif y != 5:
            print("y is not equal to 5")
            results["y is not equal to 5"] += 1
        else:
            print("None of the conditions are met")
            results["None of the conditions are met"] += 1

    print("Stats:")
    for k, v in results.items():
        print(f"{k}: {v}")

if __name__ == "__main__":
    main()