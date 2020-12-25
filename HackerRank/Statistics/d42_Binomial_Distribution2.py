# https://www.hackerrank.com/challenges/s10-binomial-distribution-2/problem

import math

# def fact(n):
#     return 1 if n == 0 else n*fact(n-1)


def comb(n, x):
    return math.factorial(n) / (math.factorial(x) * math.factorial(n - x))


def b(x, n, p):
    return comb(n, x) * p**x * (1 - p)**(n - x)


p, n = list(map(int, input().split(" ")))
ans1 = round(sum([b(i, n, p / 100) for i in range(3)]), 3)
ans2 = round(sum([b(i, n, p / 100) for i in range(2, n + 1)]), 3)

print(ans1)
print(ans2)
