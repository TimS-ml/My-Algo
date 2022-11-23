'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

Feedback
- edge case in b search
- what you need in first round search:
    - find_rotate_index <=> smallest element in the array
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if target == nums[0]:
                return 0
            else:
                return -1

        l, r = 0, len(nums)-1
        mid = l + (r - l) // 2
        while l <= r:
            if nums[l] <= nums[mid]:
                l = mid
            else:
                r = mid
            if nums[mid] < nums[l]:
                r = mid
            else:
                l = mid

        midpoint = l
        # mid at l
        def search(l, r):
            mid = l + (r - l) // 2
            while l <= r:
                if nums[l] < target:
                    l = mid
                elif target < nums[l]:
                    r = mid
                else:
                    return l
            return -1

        left = search(l, midpoint)
        right = search(midpoint+1, r)
        if left != -1:
            return left
        elif right != -1:
            return right
        else:
            return -1
