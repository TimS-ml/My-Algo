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

x, y = [], []
for _ in range(n):
    data = input().strip().split(' ')
    x.append(data[0:m])
    y.append(data[-1])

X = np.array(x, float)
y = np.array(y, float)

q = int(input().strip())
X_query = []
for _ in range(q):
    X_query.append(input().strip().split(' '))
X_query = np.array(X_query, float)

X_R = X - np.mean(X, axis=0)
y_R = y - np.mean(y)

beta = np.dot(np.linalg.inv(np.dot(X_R.T, X_R)), np.dot(X_R.T, y_R))

X_query_R = X_query - np.mean(X, axis=0)
y_query_R = np.dot(X_query_R, beta)
y_query = y_query_R + np.mean(y)

for i in y_query:
    print(round(float(i), 2))
