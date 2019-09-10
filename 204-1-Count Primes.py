# https://leetcode-cn.com/problems/count-primes/
# 埃拉托色尼筛选法


class Solution:
    def find_primes(self, n):
        primes = []
        for i in range(2, n+1):
            primes.append(i)

        for i in range(2, int(n**0.5)+1):
            for j in primes:
                if j % i == 0 and j / i > 1:
                    primes.remove(j)
        return primes

    def countPrimes(self, n) -> int:
        if n <= 2:
            return 0
        ans = self.find_primes(n-1)
        return len(ans)


# n = 499979
n = 16
print(Solution().find_primes(n))
print(Solution().countPrimes(n))
