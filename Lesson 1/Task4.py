# Task 4
L = ['abc', 'xyz', 'aba', '1221']
counter = 0
for word in L:
    if (len(word) >= 2) and (word[0] == word[-1]):
        counter += 1
print(counter)
