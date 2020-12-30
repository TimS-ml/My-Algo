# https://www.hackerrank.com/challenges/s10-multiple-linear-regression/tutorial
# https://scikit-learn.org/stable/modules/linear_model.html
# You are not expected to account for bias and variance trade-offs

# import warnings
# warnings.filterwarnings("ignore", category=DeprecationWarning)

from sklearn import linear_model
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

lm = linear_model.LinearRegression()
lm.fit(X, y)
y_query = lm.predict(X_query)  # y predict

for i in y_query:
    print(round(float(i), 2))
