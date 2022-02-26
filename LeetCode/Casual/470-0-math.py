'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()


(randX() - 1)*Y + randY() 可以等概率的生成[1, X * Y]范围的随机数
'''

# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7


class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        n = rand7()
        while n > 5:
            n = rand7()
        i = rand7()
        while i == 4:
            i = rand7()
        if i < 4:
            j = 0
        else:
            j = 5
        return n + j
