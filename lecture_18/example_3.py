
my_file = open("my_dir/hi.txt")

print("-" * 100)
for line in my_file:
    if "GB" in line:
        print(line)
        break
print("-" * 100)

my_file.close()
