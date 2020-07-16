# https://leetcode-cn.com/problems/count-primes/
# 埃拉托色尼筛选法


class Solution:
    def find_primes(self, n, primes):
        for i in range(2, n):
            if primes[i] == 1:
                j = i * i  # 从j^2开始
                if j >= n:
                    return primes
                while j < n:
                    primes[j] = 0
                    j += i
        return primes

    def countPrimes(self, n):
        if n < 2:
            return 0
        primes = [1] * n
        primes[0] = 0
        primes[1] = 0
        self.find_primes(n, primes)

        # 输出质数
        # for i in range(0, n):
        #     if primes[i] == 1:
        #         print(i)

        return sum(primes)


n = 16
print(Solution().countPrimes(n))
