'''
# Code Explain:
- Time complexity: O(logN)
- Space complexity: O(1)

lc 34
'''

# [left, right)
def find_range(self, nums, target):
    if len(nums) == 0:
        return [-1, -1]
    ans = []

    # left bound
    left, right = 0, len(nums)
    key = -1
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            key = mid
            right = mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid

    # if left == len(nums) or nums[left] != target:
    #     return [-1, -1]
    if key == -1:
        return [-1, -1]
    ans.append(left)

    # right bound
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid

    ans.append(left - 1)
    
    return ans
