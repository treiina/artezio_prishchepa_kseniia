# Task 2
a, b, c = int(input()), int(input()), int(input())
counter = 0
for i in range(a+1, b):
    if i % c == 0:
        counter += 1
print(counter)
