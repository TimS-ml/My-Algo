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


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(x, y):
            return int(y + x) - int(x + y)

        nums = sorted(map(str, nums), key=cmp_to_key(compare))
        if nums[0] == '0':
            return '0'
        else:
            return ''.join(nums)


nums = [3, 30, 34, 5, 9]
print(Solution().largestNumber(nums))
