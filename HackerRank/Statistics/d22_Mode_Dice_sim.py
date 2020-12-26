# https://www.hackerrank.com/challenges/s10-mcq-2/forum

import random

random.seed(2021)

sums = []
for _ in range(1000):
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    if d1 != d2:
        sums.append(d1 + d2)

prob = sum(i == 6 for i in sums) / 1000
print(prob)
