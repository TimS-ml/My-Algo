# https://www.hackerrank.com/challenges/s10-normal-distribution-1/problem
# https://en.wikipedia.org/wiki/Normal_distribution
# error function:
# https://docs.python.org/3/library/math.html#math.erf
# https://en.wikipedia.org/wiki/Error_function
# https://stats.stackexchange.com/questions/187828/how-are-the-error-function-and-standard-normal-distribution-function-related

# X ~ N(miu, stdev)
# x = number of successful outcome
# P(X < x) = 0.5 + 0.5*math.erf((x-miu)/(stdev * 2**0.5))
# Note: P(X < x) = P(X <= x) because P(X = x) = 0 for continuous probability distribution function
# P(a < X < b) = P(X < b) - P(X < a)

import math

miu, stdev = map(float, input().split())
lim_a = float(input())
lim_b1, lim_b2 = map(float, input().split())


def normal_prob(miu, stdev, x):
    return 0.5 + 0.5 * math.erf((x - miu) / (stdev * 2**0.5))


print(round(normal_prob(miu, stdev, lim_a), 3))
print(
    round(
        normal_prob(miu, stdev, lim_b2) - normal_prob(miu, stdev, lim_b1), 3))
