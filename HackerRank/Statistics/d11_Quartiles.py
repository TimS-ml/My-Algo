# https://www.hackerrank.com/challenges/s10-quartiles/problem

from statistics import median
# or we can use np.median()

n = int(input())
arr = [int(x) for x in input().split()]
arr.sort()

# t = int(len(arr) / 2)
t = n
# L: lower half; U: upper half
if len(arr) % 2 == 0:
    L = arr[:t]
    U = arr[t:]
# odd: do not include the median (the central value in the ordered list)
else:
    L = arr[:t]
    U = arr[t + 1:]

print(int(median(L)))
print(int(median(arr)))
print(int(median(U)))
