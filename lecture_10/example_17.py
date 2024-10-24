
def foo(name, *args):
    print("Name", name)
    print("args", args)


foo("Giorgi")
print("-" * 100)
foo("Tite", 1,2, 3)
print("-" * 100)
foo("Nugzar", "test", 1, "shmest", 109)



