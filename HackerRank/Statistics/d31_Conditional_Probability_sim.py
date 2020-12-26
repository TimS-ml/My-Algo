# https://www.hackerrank.com/challenges/s10-mcq-4/problem

# P(BB|B) = BB/(BG+GB+BB)
#    B  G
# B  BB GB
# G  BG GG

import random
# from fractions import Fraction

random.seed(2021)

sums = []
for _ in range(1000):
    c1 = random.randint(0, 1)  # 0 for girl, 1 for boy
    c2 = random.randint(0, 1)
    if c1 == 1 or c2 == 1:
        sums.append(c1 + c2)

prob = sum(i == 2 for i in sums) / 1000
# p_frac = Fraction(prob)
print(prob)
