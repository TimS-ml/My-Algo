'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()



- split in the middle
- shuffle
'''

from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x = nums[:n]
        y = nums[n:]
        ans = []
        for i in range(n):
            ans.append(x[i])
            ans.append(y[i])
        return ans
