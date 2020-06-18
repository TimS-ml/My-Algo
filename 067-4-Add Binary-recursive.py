# https://leetcode-cn.com/problems/add-binary/
import pysnooper


@pysnooper.snoop()
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) == 0:
            return b
        if len(b) == 0:
            return a
        if a[-1] == '1' and b[-1] == '1':
            return self.addBinary(self.addBinary(a[0:-1], b[0:-1]), '1') + '0'
        if a[-1] == '0' and b[-1] == '0':
            return self.addBinary(a[0:-1], b[0:-1]) + '0'
        else:
            return self.addBinary(a[0:-1], b[0:-1]) + '1'


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
