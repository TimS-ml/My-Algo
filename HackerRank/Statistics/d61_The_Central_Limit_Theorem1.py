# https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-1/problem
# https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-1/tutorial
# https://en.wikipedia.org/wiki/Central_limit_theorem
# For large n, the distribution of sample sums S is close to normal distribution
# S ~ N(miu_S, stdev_S) approximately

import math

weight_limit = float(input())
n = int(input())
miu = float(input())
stdev = float(input())


def normal_prob(miu, stdev, x):
    return 0.5 + 0.5 * math.erf((x - miu) / (stdev * 2**0.5))


miu_S = n * miu
stdev_S = (n**0.5) * stdev

# To find P(S < weight_limit)
print('%.4f' % normal_prob(miu_S, stdev_S, weight_limit))
