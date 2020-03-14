# https://leetcode-cn.com/problems/add-binary/
import pysnooper


@pysnooper.snoop()
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans, carry = '', 0
        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0 or carry:
            curval = (i >= 0 and a[i] == '1') + (j >= 0 and b[j] == '1')
            carry, rem = divmod(curval + carry, 2)
            ans = str(rem) + ans
            i -= 1
            j -= 1
        return ans


# 10101
a1 = '1010'
b1 = '1011'

# 100
a2 = '11'
b2 = '1'

# 110010
a3 = "110010"
b3 = "100"

print(Solution().addBinary(a3, b3))
