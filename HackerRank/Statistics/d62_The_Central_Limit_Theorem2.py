# https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-2/problem

import math

ticket_limit = float(input())
n = int(input())
miu = float(input())
stdev = float(input())


def normal_prob(miu, stdev, x):
    return 0.5 + 0.5 * math.erf((x - miu) / (stdev * 2**0.5))


miu_S = n * miu
stdev_S = (n**0.5) * stdev

# To find P(S < ticket_limit)
print('%.4f' % normal_prob(miu_S, stdev_S, ticket_limit))
