# Task 4
def my_range(start: int, stop=None, step=1):
    if stop is None:
        stop = start
        start = 0
    lst = []
    while start < stop:
        lst.append(start)
        start += step
    return lst


print(list(range(2, 12, 3)))
print(list(my_range(2, 12, 3)))
