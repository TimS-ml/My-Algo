'''
# Code Explain:
- Time complexity: O(logN)
- Space complexity: O(1)

- All are ascending arrays except for a sudden drop at a certain point

case1: [5, 6, 7, 1, 2, 3, 4]
                 |
                mid

case2: [5, 6, 7, 8, 2, 3, 4]
                 |
                mid

- find out the sudden drop location
    - if mid < start, then sudden drop at [l, mid]
        - [mid, r] is the asc array
        - mid < t < r check is ok (in asc seq)
            - but we cannot use l < t (case3)
    - if mid > start, then sudden drop at [mid, r]

case3: [5, 6, 7, 8, 2, 3, 4]
        |     |           |
        l    mid          r

for l < t, it could be in both left of mid or right of mid (t = 6 or t = 8)
for mid < t < r, it must be in right side of mid


- If [left, mid-1] is an ascending ordered array, and 'target' in [nums[left], nums[mid])
    - then we should narrow the search scope to [left, mid-1], otherwise, search in [mid+1, right]
- If [mid, right] is an ascending ordered array, and 'target' in (nums[mid+1], nums[right]]
    - then we should narrow the search range to [mid+1, right], otherwise we should search in [left, mid-1].
'''

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        # init 2 pointers
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid  # this is the only place to return answer

            # update l and r, we can skip 'mid' since we already know mid != target
            # [0, mid] is ascending order, sudden drop in [mid, end]
            if nums[0] <= nums[mid]:
                # tartget in ascending range
                if nums[0] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:  # sudden drop in [0, mid], [mid, end] is ascending order
                # tartget in ascending range
                if nums[mid] < target <= nums[len(nums) - 1]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
