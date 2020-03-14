# https://leetcode-cn.com/problems/add-binary/
# This is the fastest sol by far, and this is smart
# Similar to sol2
import pysnooper


@pysnooper.snoop()
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        ans = ''

        a = list(a)
        b = list(b)

        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())

            ans += str(carry % 2)
            carry //= 2

        return ans[::-1]


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
