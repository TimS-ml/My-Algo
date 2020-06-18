# https://leetcode-cn.com/problems/count-primes/
# 埃拉托色尼筛选法


class Solution:
    def find_primes(self, n):
        primes = [1] * n  # 0-(n-1)
        primes[0] = 0
        primes[1] = 0
        for i in range(2, int(n**0.5) + 1):
            if primes[i] == 1:  # 加了if就缩短了一半的时间
                # print('i', i)
                j = i**2
                if j >= n:  # 加了if就缩短了1/3的时间
                    return primes
                while j < n:
                    # print('j', j)
                    primes[j] = 0
                    j += i
        return primes

    def countPrimes(self, n) -> int:
        if n <= 2:
            return 0
        ans = self.find_primes(n)
        return sum(ans)


n = 16
print(Solution().find_primes(n))
print(Solution().countPrimes(n))
