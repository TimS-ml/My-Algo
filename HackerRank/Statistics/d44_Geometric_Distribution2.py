# https://www.hackerrank.com/challenges/s10-geometric-distribution-2/problem
# at least 1 defect is found during the first 5 inspections

defect = list(map(int, input().split()))
insp = int(input())

p = defect[0] / defect[1]
q = 1 - p

print(round(1 - q**5, 3))
print(round(sum([q**(insp - x) * p for x in range(1, insp + 1)]), 3))
