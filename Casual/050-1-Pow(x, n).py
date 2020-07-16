# https://leetcode-cn.com/problems/powx-n/


class Solution:
    def myPow(self, x: float, n: int) -> float:
        cache = {}

        def Pow(x, i):
            if i in cache:
                return cache[i]
            if i <= 2:
                return x**i
            else:
                ans = Pow(x, int(i / 2)) * Pow(x, i - int(i / 2))
            cache[i] = ans
            return ans

        return Pow(x, n)


x, n = 2, 10
print(Solution().myPow(x, n))
