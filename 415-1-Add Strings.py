# https://leetcode-cn.com/problems/add-strings/
# ord return number of ONE digit


class Solution:
    def addStrings(self, num1, num2):
        num1, num2 = list(num1), list(num2)
        carry, ans = 0, []
        while len(num2) > 0 or len(num1) > 0:
            n1 = ord(num1.pop())-ord('0') if len(num1) > 0 else 0
            n2 = ord(num2.pop())-ord('0') if len(num2) > 0 else 0

            temp = n1 + n2 + carry
            ans.append(temp % 10)
            carry = temp // 10
        if carry:
            ans.append(carry)
        return ''.join([str(i) for i in ans])[::-1]


num1 = '12345'
num2 = '11'
print(Solution().addStrings(num1, num2))
