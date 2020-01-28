# Task 8
from collections import Counter

D = {'qwerty': 77, 'asdfg': 23, 'vbjk': 61, 'zxcvb': 56, 'tyuio': 17, 'fghnm': 44}
D_count = Counter(D)
highest = D_count.most_common(3)
print(highest, "\n")
