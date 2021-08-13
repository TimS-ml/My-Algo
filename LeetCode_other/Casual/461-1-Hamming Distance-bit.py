# https://leetcode-cn.com/problems/hamming-distance/
# The Hamming distance between two integers
# is the number of positions at which the corresponding bits are different.


class Solution:
    def hammingDistance(self, x, y) -> int:
        print(bin(x), bin(y))
        x = x ^ y  # 按位亦或, 不同->1, 相同->0
        print(bin(x))  # x和y不同的位数显示为1
        y = 0  # use y as ANS
        while x:
            y += 1
            x = x & (x - 1)
        return y


x = 1
y = 4
print(Solution().hammingDistance(x, y))
