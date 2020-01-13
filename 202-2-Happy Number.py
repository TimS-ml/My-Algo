# leetcode-cn.com/problems/happy-number///leetcode-cn.com/problems/happy-number/i


class Solution:
    def isHappy(self, n: int) -> bool:
        n = sum([int(i)**2 for i in str(n)])
        if n > 4:
            return self.isHappy(n)
        elif n == 1:
            return True
        else:
            return False


n = 19
print(Solution().isHappy(n))
