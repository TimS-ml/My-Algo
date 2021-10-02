# https://leetcode-cn.com/problems/string-to-integer-atoi/
# https://leetcode-cn.com/problems/string-to-integer-atoi/solution/python-1xing-zheng-ze-biao-da-shi-by-knifezhu/
# max(min(number, 2**31 - 1), -2**31)

import re


class Solution:
    def myAtoi(self, str) -> int:
        return max(
            min(int(*re.findall('^[\+\-]?\d+', str.lstrip())), 2**31 - 1),
            -2**31)


s = "42"
print(Solution().myAtoi(s))
