'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

# Pros and Cons and Notation:

case:
- 30 > 2
- 48 vs 4?
    - compare [xxx, 48, 4, xxx]
    -         [xxx, 4, 48, xxx]
- 448 vs 48 vs 4?
    - compare [xxx, 48, 4, 448, xxx]
'''

from typing import List
from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(x, y):
            return int(y + x) - int(x + y)

        li = map(str, nums)
        li = sorted(li, key=cmp_to_key(compare))
        if li[0] == '0':
            return '0'
        else:
            return ''.join(li)


nums = [3, 30, 34, 5, 9]
print(Solution().largestNumber(nums))
