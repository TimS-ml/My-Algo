# https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-3/problem
# https://en.wikipedia.org/wiki/Standard_score

# Normal distribution describes that
# 68% population will fall between range +-1 stdev from mean
# 95% population will fall between range +-2 stdev from mean
# 99.7% population will fall between range +-3 stdev from mean
# Prob(m-z*s < X < m+z*s) = 0.95

n = int(input())
[miu, stdev] = [float(input()) for _ in range(2)]  # 500, 80
[prob, z] = [float(input()) for _ in range(2)]  # 0.95, 1.96

# population mean ~ N(miu, stdev)
# sample mean ~ N(miu, s), where s = sample stdev = stdev/n**0.5
s = stdev / n**0.5

print('%.2f' % (miu - z * s))
print('%.2f' % (miu + z * s))
