'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()



find idx of maximum val using binary search
or just return arr.index(max(arr))
'''

from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        left, right, ans = 1, n - 2, 0

        while left <= right:
            mid = (left + right) // 2
            if arr[mid] > arr[mid + 1]:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans
