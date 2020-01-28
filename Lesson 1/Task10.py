# Task 10
L1 = [45, 45, 86, 10, 2, 62, 2]
L2 = [85, 2, 45, 96, 56, 3]
print(list(set((set(L1)-set(L2))|(set(L2)-set(L1)))))
