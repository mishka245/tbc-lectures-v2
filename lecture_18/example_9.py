
symbols = 0
lines = 0
words = 0
with open("my_dir/task_1.txt", "r") as file:
    for line in file:
        # symbols += len(line.replace(" ", ""))
        symbols += sum(1 for c in line if c != " ")
        lines += 1
        words += len(line.split(" "))

print(f"Symbols count - {symbols}")
print(f"Lines count - {lines}")
print(f"Words count - {words}")
