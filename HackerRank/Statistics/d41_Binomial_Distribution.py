# https://www.hackerrank.com/challenges/s10-binomial-distribution-1/problem
# https://www.hackerrank.com/challenges/s10-binomial-distribution-1/tutorial
# https://en.wikipedia.org/wiki/Binomial_distribution
# https://stackoverflow.com/questions/26560726/python-binomial-coefficient

import math

# def fact(n):
#     return 1 if n == 0 else n*fact(n-1)


# we can use math.comb in python 3.8
# or scipy.special.comb
def comb(n, x):
    return math.factorial(n) / (math.factorial(x) * math.factorial(n - x))


def b(x, n, p):
    return comb(n, x) * p**x * (1 - p)**(n - x)


l, r = list(map(float, input().split(" ")))
odds = l / r
ans = round(sum([b(i, 6, odds / (1 + odds)) for i in range(3, 7)]), 3)
print(ans)
