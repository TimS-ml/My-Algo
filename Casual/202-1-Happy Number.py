# leetcode-cn.com/problems/happy-number///leetcode-cn.com/problems/happy-number/i


class Solution:
    def isHappy(self, n: int) -> bool:
        if n <= 4 and n != 1:
            return False
        while True:
            n = sum([int(i)**2 for i in str(n)])
            if n == 4:
                return False
            if n == 1:
                return True


n = 19
print(Solution().isHappy(n))
