'''
# Code Explain:
- Time complexity: O(logN)
- Space complexity: O(1)

lc 1671
extended version of binary search

case:
ans idx = 0 or -1
'''


def find_max_in_bitonic_array(nums):
    left, right = 0, len(nums)
    while left < right:
        mid = int((right + left) / 2)
        print(left, right, mid)
        if mid + 1 < len(nums) and nums[mid] > nums[mid + 1]:  # mid in DESC seq
            right = mid
        elif mid + 1 == len(nums):  # mid=l=r=len
            return mid
        else:  # still in ASC seq
            left = mid + 1

    # l = r
    # return nums[left]
    return left


def main():
    print(find_max_in_bitonic_array([1, 3, 8, 12, 4, 2]))
    print(find_max_in_bitonic_array([3, 8, 3, 1]))
    print(find_max_in_bitonic_array([1]))  # -1
    print(find_max_in_bitonic_array([1, 3, 8, 12, 16]))  # -1
    print(find_max_in_bitonic_array([10, 9, 8]))  # 0


main()

