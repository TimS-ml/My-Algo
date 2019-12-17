# https://leetcode-cn.com/problems/add-strings/
# this is more straightforward


class Solution:
    def addStrings(self, num1, num2):
        carry = 0  # carry can be 0 or 1
        i = len(num1) - 1
        j = len(num2) - 1
        ans = ''

        for k in range(max(i, j) + 1):
            a = int(num1[i]) if i >= 0 else 0
            b = int(num2[j]) if j >= 0 else 0
            i, j = i - 1, j - 1
            sum = a + b + carry
            carry = 0

            if sum >= 10:
                carry = 1
                ans += str(sum - 10)
            else:
                ans += str(sum)

        # if still carry (99+1)
        if carry == 1:
            ans += '1'

        return ans [::-1]


# num1 = '12345'
# num2 = '11'
# num1 = '99'
# num2 = '1'
num1 = '88'
num2 = '12'
print(Solution().addStrings(num1, num2))
