# https://www.hackerrank.com/challenges/s10-least-square-regression-line/problem

x, y = [], []
for _ in range(5):
    i = input().split()
    x.append(int(i[0]))
    y.append(int(i[1]))

n = len(x)
x_sum = sum(x)
x_sum_sqr = x_sum**2
x_sqr_sum = sum([x_i**2 for x_i in x])
y_sum = sum(y)

sum_prod_xy = 0
for x_i, y_i in zip(x, y):
    sum_prod_xy += (x_i * y_i)

b = (n * sum_prod_xy - x_sum * y_sum) / (n * x_sqr_sum - x_sum_sqr)
y_mean = y_sum / n
x_mean = x_sum / n
a = y_mean - b * x_mean

# to make prediction
x_test = 80
y_test = a + b * x_test
print("%.3f" % y_test)  # 78.288
