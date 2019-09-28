# https://leetcode-cn.com/problems/hamming-distance/
# The Hamming distance between two integers 
# is the number of positions at which the corresponding bits are different.


class Solution:
    def hammingDistance(self, x, y) -> int:
        x = x ^ y
        y = 0
        while x:
            y += 1
            x = x & (x - 1)
        return y
