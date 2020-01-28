# Task 2
print("Введите строку: ")
S = input()
S_chars = {c: S.count(c) for c in set(S)}
print(S_chars)
