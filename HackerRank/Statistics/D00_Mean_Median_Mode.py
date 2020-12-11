# https://www.hackerrank.com/challenges/s10-basic-statistics/problem
# Other than the modal value (which will always be an integer), your answers should be in decimal form, rounded to a scale of  decimal place

import numpy as np
from scipy import stats

size = int(input())
numbers = list(map(int, input().split()))

print(np.mean(numbers))
print(np.median(numbers))
print(int(stats.mode(numbers)[0]))
