from scipy.stats import binom

import math

# def fact(n):
#     return 1 if n == 0 else n*fact(n-1)


# we can use math.comb in python 3.8
# or scipy.special.comb
def comb(n, x):
    return math.factorial(n) / (math.factorial(x) * math.factorial(n - x))


def b(x, n, p):
    return comb(n, x) * p**x * (1 - p)**(n - x)

print(b(1, 6, 0.5))
print(binom.cdf(1, 6, 0.5))
