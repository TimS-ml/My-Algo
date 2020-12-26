# https://www.hackerrank.com/challenges/s10-poisson-distribution-1/problem
# https://www.hackerrank.com/challenges/s10-poisson-distribution-1/tutorial
# https://en.wikipedia.org/wiki/Poisson_distribution

from math import factorial, exp

miu = float(input())
x = int(input())
prob = ((miu ** x) * exp(-miu)) / factorial(x)
print(round(prob, 3))
