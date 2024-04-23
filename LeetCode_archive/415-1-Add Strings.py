# https://leetcode-cn.com/problems/add-strings/
# ord return number of ONE digit


class Solution:
    def addStrings(self, num1, num2):
        num1, num2 = list(num1), list(num2)
        carry, ans = 0, []
        while len(num2) > 0 or len(num1) > 0:
            n1 = ord(num1.pop()) - ord('0') if len(num1) > 0 else 0
            n2 = ord(num2.pop()) - ord('0') if len(num2) > 0 else 0

            temp = n1 + n2 + carry
            ans.append(temp % 10)
            carry = temp // 10
        if carry:
            ans.append(carry)
        return ''.join([str(i) for i in ans])[::-1]

    def addStrings_2(self, num1, num2):
        nums1 = list(num1)
        nums2 = list(num2)
        ans, carry = [], 0

        while nums1 or nums2:
            n1 = n2 = 0
            if nums1:
                n1 = ord(nums1.pop()) - ord('0')
            if nums2:
                n2 = ord(nums2.pop()) - ord('0')

            carry, remain = divmod(n1 + n2 + carry, 10)
            ans.append(remain)

        if carry:
            ans.append(carry)
        return ''.join(str(d) for d in ans)[::-1]

    def addStrings_3(self, num1, num2):
        carry = 0  # carry can be 0 or 1
        i = len(num1) - 1
        j = len(num2) - 1
        ans = ''

        for k in range(max(i, j) + 1):
            a = int(num1[i]) if i >= 0 else 0
            b = int(num2[j]) if j >= 0 else 0
            i, j = i - 1, j - 1

            # S = a + b + carry
            # carry = 0

            # if S >= 10:
            #     carry = 1
            #     ans += str(S - 10)
            # else:
            #     ans += str(S)
            carry, S = divmod(a + b + carry, 10)
            ans += str(S)

        # if still carry (99+1)
        if carry == 1:
            ans += '1'

        return ans[::-1]


num1 = '12345'
num2 = '11'
print(Solution().addStrings(num1, num2))
