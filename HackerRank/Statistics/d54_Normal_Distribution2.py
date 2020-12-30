# https://www.hackerrank.com/challenges/s10-normal-distribution-2/problem
# X ~ N(miu, stdev)
# x = number of successful outcome
# P(X < x) = 0.5 + 0.5*math.erf((x-miu)/(stdev * 2**0.5))
# Note: P(X < x) = P(X <= x) because P(X = x) = 0 for continuous probability distribution function
# P(a < X < b) = P(X < b) - P(X < a)
# P(X > c) = 1 - P(X < c)
# output percentage

import math

miu, stdev = map(float, input().split())
lim_1 = float(input())
lim_2 = float(input())


def normal_prob(miu, stdev, x):
    return 0.5 + 0.5 * math.erf((x - miu) / (stdev * 2**0.5))


print('%.2f' % ((1 - normal_prob(miu, stdev, lim_1)) * 100))
print('%.2f' % ((1 - normal_prob(miu, stdev, lim_2)) * 100))
print('%.2f' % (normal_prob(miu, stdev, lim_2) * 100))
