# https://www.hackerrank.com/challenges/s10-binomial-distribution-2/problem

from scipy.special import comb

def b(x, n, p):
    return comb(n, x) * p**x * (1 - p)**(n - x)


p, n = list(map(int, input().split(" ")))
ans1 = round(sum([b(i, n, p / 100) for i in range(3)]), 3)
ans2 = round(sum([b(i, n, p / 100) for i in range(2, n + 1)]), 3)

print(ans1)
print(ans2)
