'''
# Code Explain:
- Time complexity: O(logN)
- Space complexity: O(1)

'''


def search_min_diff_element(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return nums[mid]
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid

    # left == right, edge case: =0 or =len(nums) -> out of bound
    # print(f'left {left}, right {right}')
    if left != len(nums) and (nums[left] - target) < (target - nums[right]):
        return nums[left]
    else:
        return nums[right-1]


def main():
    print(search_min_diff_element([4, 6, 10], 7))
    print(search_min_diff_element([4, 6, 10], 4))
    print(search_min_diff_element([1, 3, 8, 10, 10, 15], 12))
    print(search_min_diff_element([4, 6, 10], 17))


main()
