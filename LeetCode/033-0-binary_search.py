'''
# Code Explain:
- Time complexity: O(logn)
- Space complexity: O(1)


- The array itself is not ordered. After the rotation, only the parts of the array are guaranteed to be ordered
    - All are ascending arrays except for a sudden drop at a certain point

case: [7, 0, 1, 2] mid is 1, target is 7
we cannot use target vs mid to locate array
so
[1] make sure [left, mid] or [mid, right] is ascending order array
[2] check if tartget inside that ascending array

    nums[0] <= target <= nums[mid]
               target <= nums[mid] < nums[0]
                         nums[mid] < nums[0] <= target

what we need to compare
(nums[0] <= target),  (target <= nums[mid]) , (nums[mid] < nums[0])

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
