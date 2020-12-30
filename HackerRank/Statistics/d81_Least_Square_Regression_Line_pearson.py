# https://www.hackerrank.com/challenges/s10-least-square-regression-line/problem

from statistics import mean, pstdev


def pearson(x, y):
    n = len(x)
    mx, sx, my, sy = mean(x), pstdev(x), mean(y), pstdev(y)
    return sum((xi - mx) * (yi - my) for xi, yi in zip(x, y)) / (n * sx * sy)


def linear_regression(x, y):
    b = pearson(x, y) * pstdev(y) / pstdev(x)
    return mean(y) - b * mean(x), b


x, y = [], []
for _ in range(5):
    i = input().split()
    x.append(int(i[0]))
    y.append(int(i[1]))
a, b = linear_regression(x, y)

# to make prediction
x_test = 80
y_test = a + b * x_test
print("%.3f" % y_test)  # 78.288
