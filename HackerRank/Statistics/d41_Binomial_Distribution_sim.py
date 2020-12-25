# https://www.hackerrank.com/challenges/s10-binomial-distribution-1/problem
# https://numpy.org/doc/stable/reference/random/generated/numpy.random.binomial.html

import numpy as np


l, r = list(map(float, input().split(" ")))
odds = l / r
ans = round(sum(np.random.binomial(6, odds / (1 + odds), 10000) >= 3)/10000, 3)
print(ans)
