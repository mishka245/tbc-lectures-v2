
# გამარტივებული მაგალითია for/else კონსტრუქციის საჩვენებლად

for i in range(1, 20):
    if i % 17 == 0:
        print(f"17-ის ჯერადი რიცხვია : {i}, ცდების რაოდენობა - {i}")
        break
else:
    print("ვერ ვიპოვეთ")
