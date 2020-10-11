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

    def addBinary2(self, a: str, b: str) -> str:
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

    def addBinary3(self, a: str, b: str) -> str:
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

    # This is the fastest sol by far, and this is smart
    def addBinary4(self, a: str, b: str) -> str:
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
