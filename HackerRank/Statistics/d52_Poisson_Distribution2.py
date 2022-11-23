# https://www.hackerrank.com/challenges/s10-poisson-distribution-2/problem#
# Given cost_A = 160 + 40*X**2
# E(cost_A) = E(160 + 40*X**2)
#   = E(160) + E(40*X**2)
#   = 160 + 40*E(X**2)
# By definition, E(X**2) = E(X) + (E(X))**2 and E(X) = miu_A

miu_A, miu_B = map(float, input().split())

cost_A = 160 + 40*(miu_A + miu_A**2)
print(round(cost_A, 3))

cost_B = 128 + 40*(miu_B + miu_B**2)
print(round(cost_B, 3))
