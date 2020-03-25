# https://leetcode-cn.com/problems/add-binary/
import pysnooper


@pysnooper.snoop()
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n)
        print(a, b)

        carry = 0
        ans = []
        for i in range(n - 1, -1, -1):
            if a[i] == '1':
                carry += 1
            if b[i] == '1':
                carry += 1

            if carry % 2 == 1:
                ans.append('1')
            else:
                ans.append('0')
            carry //= 2

        if carry == 1:
            ans.append('1')
        ans.reverse()

        return ''.join(ans)


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
