'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()



case: 100
100 / 7 = 14 ... 2
14 / 7 = 2 ... 0
ans = 2 * 7**2 + 0 * 7**1 + 2 * 7**0
'''

from collections import deque


class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        sign = -1 if num < 0 else 1
        num = abs(num)
        ans = ''

        while num != 0:
            num, reminder = divmod(num, 7)
            ans = str(reminder) + ans

        if sign == -1:
            return '-' + ans
        else:
            return ans

    def convertToBase7_2(self, num: int) -> str:
        if num < 0:
            return '-' + self.convertToBase7_2(-1 * num)
        if num < 7:
            return str(num)
        return self.convertToBase7_2(int(num // 7)) + \
               self.convertToBase7_2(num % 7)


num = 100
num = -7
print(Solution().convertToBase7_2(num))
