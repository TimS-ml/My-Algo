# https://leetcode-cn.com/problems/add-strings/
# a slightly better one


class Solution:
    def addStrings(self, num1, num2):
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


num1 = '12345'
num2 = '11'
print(Solution().addStrings(num1, num2))
