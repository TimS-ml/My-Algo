# https://leetcode-cn.com/problems/add-binary/


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = list(map(int, a)), list(map(int, b))
        a.reverse()
        b.reverse()
        if len(a) < len(b):
            a, b = b, a
        carry = 0
        for i in range(len(b)):
            print(a[i], b[i], carry)
            digit = (a[i] + b[i] + carry) % 2
            carry = (a[i] + b[i] + carry) // 2
            a[i] = digit
        for i in range(len(b), len(a)):
            print(a[i], carry)
            digit = (a[i] + carry) % 2
            carry = (a[i] + carry) // 2
            a[i] = digit
        a.reverse()
        if carry == 1:
            a = [1] + a
        return ''.join([str(i) for i in a])


# 10101
a1 = '1010'
b1 = '1011'

# 100
a2 = '11'
b2 = '1'

# 110010
a3 = "110010"
b3 = "100"

print(Solution().addBinary(a2, b2))
