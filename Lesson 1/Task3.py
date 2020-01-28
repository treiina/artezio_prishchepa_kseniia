# Task 3
print("Введите строку: ")
S = input()
if len(S) < 2:
    print('Emp')
else:
    print(S[:2], S[-2], S[-1], sep='')
