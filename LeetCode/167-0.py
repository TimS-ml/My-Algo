'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()



'''

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            if target - numbers[l] - numbers[r] > 0:
                l += 1
            elif target - numbers[l] - numbers[r] < 0:
                r -= 1
            else:
                return [l + 1, r + 1]
