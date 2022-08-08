'''
# Code Explain:
- Time complexity: O(logN)
- Space complexity: O(1)

- sorted array, don't know order
- asc or desc
- number exsit or not exsit
- number have dupl

we cannot do arr = arr[::-1]
since the time complexity is O(n)

lc 704
'''

# [l, r)
def binary_search(nums, target):
    isAsc = nums[0] < nums[-1]
    left, right = 0, len(nums)

    while left < right:
        mid = int(left + (right - left) // 2)  # this is better
        
        if isAsc:
            if target < nums[mid]:  # target at left half, reduce right
                right = mid
            elif target > nums[mid]:  # target at right half, increase left
                left = mid + 1
            else:  # arr[mid] == key
                return mid
        else:  # !!! change < to >, > to <
            if target > nums[mid]:
                right = mid
            elif target < nums[mid]:
                left = mid + 1
            else:  # arr[mid] == key
                return mid

    return -1


def main():
    print(binary_search([4, 6, 10], 10))
    print(binary_search([1, 2, 3, 4, 5, 6, 7], 5))
    print(binary_search([10, 6, 4], 10))
    print(binary_search([10, 6, 4], 4))


main()

