# https://leetcode-cn.com/problems/plus-one/


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        sdigits = sum(d*(10**i) for i, d in enumerate(digits[::-1])) 
        # print(sdigits)
        sdigits = int(sdigits) + 1
        ans = list(str(sdigits))
        return ans


# digits = [1, 2, 3]
digits = [9, 9, 9]
print(Solution().plusOne(digits))
