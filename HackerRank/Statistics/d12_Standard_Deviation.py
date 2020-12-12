# https://www.hackerrank.com/challenges/s10-standard-deviation/problem

n = int(input())
x = sorted(list(map(int, input().split())))
mean = sum(x) / n
variance = sum([((x - mean)**2) for x in x]) / n
stddev = variance**0.5
print(round(stddev, 1))
