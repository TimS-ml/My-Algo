# https://www.hackerrank.com/challenges/s10-multiple-linear-regression/tutorial
# Compute the inverse of a matrix.
# https://numpy.org/doc/stable/reference/generated/numpy.linalg.inv.html#numpy.linalg.inv
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.inv.html#scipy.linalg.inv
# You are not expected to account for bias and variance trade-offs

# There is no need for normalization(If you did, the error would be intolerable.)
# But it's okay for X and Y to be centered in case the problem of scale,
# while you don't need to add constant column to X.

import numpy as np

[m, n] = list(map(int, input().split()))

data = np.empty((n, m + 2))
data[:, 0] = 1
data[:, 1:] = [list(map(float, input().split())) for _ in range(n)]
X = data[:, :-1]
y = data[:, -1]

q = int(input())
X_query = np.empty((q, m + 1))
X_query[:, 0] = 1
X_query[:, 1:] = [list(map(float, input().split())) for _ in range(q)]

beta = np.dot(np.linalg.inv(np.dot(X.T, X)), np.dot(X.T, y))

print('\n'.join(map(str, np.round(np.dot(X_query, beta), 2))))
