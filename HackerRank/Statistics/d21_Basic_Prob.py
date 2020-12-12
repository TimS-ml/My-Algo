# https://www.hackerrank.com/challenges/s10-mcq-1/forum
# https://www.jeffastor.com/blog/using-python-to-calculate-dice-statistics
# https://www.geeksforgeeks.org/python-number-of-values-greater-than-k-in-list/

import random
from functools import reduce

random.seed(2021)

sums = []
for _ in range(1000):
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    sums.append(d1 + d2)

# prob = sum(i <= 9 for i in sums)  / len(sums)
prob = reduce(lambda s, j: s + (1 if j <= 9 else 0), sums, 0) / len(sums)
print(prob)
