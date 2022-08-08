'''
# Code Explain:
- Time complexity: O(logN)
- Space complexity: O(1)

- find ceiling (smallest element in the given array greater than or equal to the ‘key’)

lc 35
'''

# [l, r)
def search_ceiling_of_a_number(nums, target):
    left, right = 0, len(nums)

    while left < right:
        mid = int((left + right) // 2)
        
        print(left, right, mid)
        if target < nums[mid]:
            right = mid
        elif target > nums[mid]:
            left = mid + 1
        else:  # key == arr[mid+1]
            return mid

    # this is different, end of loop: l = r = 0 or = -1
    return left


def main():
    print(search_ceiling_of_a_number([4, 6, 10], 6))
    print(search_ceiling_of_a_number([1, 3, 8, 10, 15], 12))
    print(search_ceiling_of_a_number([4, 6, 10], 17))
    print(search_ceiling_of_a_number([4, 6, 10], -1))


main()

