# https://leetcode-cn.com/problems/plus-one/


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # ''.join(xxx)是str，转int之后+1，再转str以变回数组
        ans = str(int(''.join([str(a) for a in digits])) + 1)
        # print(''.join([str(a) for a in digits]))
        return [int(i) for i in ans]


# digits = [1, 2, 3]
digits = [9, 9, 9]
print(Solution().plusOne(digits))
