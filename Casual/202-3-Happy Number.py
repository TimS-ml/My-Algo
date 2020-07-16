# leetcode-cn.com/problems/happy-number///leetcode-cn.com/problems/happy-number/i


class Solution:
    def bitSquareSum(self, n):
        return sum([int(i)**2 for i in str(n)])

    def isHappy(self, n: int) -> bool:
        slow = n
        fast = n
        if n > 4:
            slow = self.bitSquareSum(slow)
            fast = self.bitSquareSum(fast)
            fast = self.bitSquareSum(fast)
        while slow != fast:
            slow = self.bitSquareSum(slow)
            fast = self.bitSquareSum(fast)
            fast = self.bitSquareSum(fast)
        return slow == 1


n = 19
print(Solution().isHappy(n))
