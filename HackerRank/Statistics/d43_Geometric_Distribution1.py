# https://www.hackerrank.com/challenges/s10-geometric-distribution-1/problem
# https://en.wikipedia.org/wiki/Geometric_distribution
# https://en.wikipedia.org/wiki/Bernoulli_trial
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.geom.html
# https://numpy.org/doc/stable/reference/random/generated/numpy.random.geometric.html

from scipy.stats import geom

defect = list(map(int, input().split()))
insp = int(input())

p = defect[0] / defect[1]
# q = 1 - p
# print(round(q**(insp-1) * p, 3))

print(round(geom.pmf(insp, p), 3))
