# https://www.hackerrank.com/challenges/s10-mcq-3/forum

import itertools
from fractions import Fraction

x = ['b'] * 3 + ['r'] * 4
y = ['b'] * 4 + ['r'] * 5
z = ['b'] * 4 + ['r'] * 4

r = [(i) for i in itertools.product(x, y, z)]
e = list(map(lambda x: x.count('r') == 2 and x.count('b') == 1, r))
p_frac = Fraction(e.count(True), len(e))
print(p_frac)
