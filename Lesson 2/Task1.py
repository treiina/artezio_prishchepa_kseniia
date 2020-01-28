# Task 1
X = int(input())
counter = 0
for i in range(X):
    if i % 2 == 1:
        print(i*i)
        counter += 1
print("Количество таких чисел: ", counter)
