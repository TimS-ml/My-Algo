# https://www.hackerrank.com/challenges/s10-mcq-4/problem

# P(BB|B) = BB/(BG+GB+BB)
#    B  G
# B  BB GB
# G  BG GG

import random

random.seed(2021)

sums = []
for _ in range(1000):
    c1 = random.randint(0, 1)  # 0 for girl, 1 for boy
    c2 = random.randint(0, 1)
    if d1 != d2:
        sums.append(d1 + d2)

prob = sum(i == 6 for i in sums) / 1000
print(prob)

