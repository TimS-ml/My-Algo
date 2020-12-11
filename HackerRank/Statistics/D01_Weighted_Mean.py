# https://www.hackerrank.com/challenges/s10-weighted-mean/problem

n = int(input())
numbers = list(map(int, input().split()))
weight = list(map(int, input().split()))
print(
    round(1.0 * sum([numbers[i] * weight[i] for i in range(n)]) / sum(weight),
          1))
