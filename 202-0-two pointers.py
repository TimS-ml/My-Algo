'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

# Pros and Cons and Notation:

'''


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

    def isHappy_2(self, n: int) -> bool:
        n = sum([int(i)**2 for i in str(n)])
        if n > 4:
            return self.isHappy_2(n)
        elif n == 1:
            return True
        else:
            return False

    def bitSquareSum(self, n):
        return sum([int(i)**2 for i in str(n)])

    def isHappy_3(self, n: int) -> bool:
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
