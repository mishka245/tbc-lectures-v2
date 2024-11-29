import timeit

# Append method
def using_append():
    result = []
    for i in range(10_000):
        result.append(i * 2)
    return result

# List comprehension
def using_list_comprehension():
    return [i * 2 for i in range(10_000)]

# Preallocated list with indexing
def using_preallocated():
    n = 10_000
    result = [None] * n
    for i in range(n):
        result[i] = i * 2
    return result

# Timing the methods
print("Using append:", timeit.timeit("using_append()", globals=globals(), number=1000))
print("Using list comprehension:", timeit.timeit("using_list_comprehension()", globals=globals(), number=1000))
print("Using preallocated list:", timeit.timeit("using_preallocated()", globals=globals(), number=1000))