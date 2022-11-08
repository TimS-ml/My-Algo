class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        n1, n2 = 2, 3

        # from 4 to n
        for i in range(4, n + 1):
            temp = n1 + n2
            n1 = n2  # old n2
            n2 = temp  # old n1 + old n2
        return n2
