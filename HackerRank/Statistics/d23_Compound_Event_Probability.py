# https://www.hackerrank.com/challenges/s10-mcq-3/forum
# https://docs.python.org/3/library/itertools.html#itertools.product

import itertools
from fractions import Fraction

x = ['b'] * 3 + ['r'] * 4
y = ['b'] * 4 + ['r'] * 5
z = ['b'] * 4 + ['r'] * 4

# list all possibel combinations
r = [(i) for i in itertools.product(x, y, z)]
e = list(map(lambda x: x.count('r') == 2 and x.count('b') == 1, r))
p_frac = Fraction(e.count(True), len(e))
print(p_frac)


# x = [4, 3]
# y = [5, 4]
# z = [4, 4]

# # The probabilities of pulling red form each urn
# xr = x[0] / sum(x)
# yr = y[0] / sum(y)
# zr = z[0] / sum(z)

# p = (xr * yr * (1 - zr)) + (xr * (1 - yr) * zr) + ((1 - xr) * yr * zr)
# p_frac = Fraction(p).limit_denominator()
# print(p_frac)
