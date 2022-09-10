'''
# Code Explain:
- Time complexity: O(logN)
- Space complexity: O(1)

lc 1095, 852

why find middle first? why not one pass bindary search directly?
case:
1, 2, 3, 4, 9, 8, 7
      |        |
     mid     target

since peak is max(nums), why use binary search find peak?
list.index is O(n)

thus
- find mid point
- two binary search
'''


def search_bitonic_array(nums, target):
    def find_max(nums):
        start, end = 0, len(nums) - 1
        while start < end:
            mid = start + (end - start) // 2
            if nums[mid] > nums[mid + 1]:
                end = mid
            else:
                start = mid + 1
    
        # at the end of the while loop, 'start == end'
        return start

    def binary_search(nums, target, start, end, isAsc=True):
        while start < end:
            mid = int(start + (end - start) / 2)
    
            if target == nums[mid]:
                return mid
    
            if isAsc:  # ascending order
                if target < nums[mid]:
                    end = mid
                else:  # target > arr[mid]
                    start = mid + 1
            else:  # descending order
                if target > nums[mid]:
                    end = mid
                else:  # target < arr[mid]
                    start = mid + 1
    
        return -1  # element is not found

    maxIndex = find_max(nums)

    # 0 ~ mid idx
    keyIndex = binary_search(nums, target, 0, maxIndex + 1)
    if keyIndex != -1:
        return keyIndex
    else:
        # mid idx ~ end
        return binary_search(nums, target, maxIndex + 1, len(nums), False)


def main():
    print(search_bitonic_array([1, 3, 8, 4, 3], 4))
    print(search_bitonic_array([3, 8, 3, 1], 8))
    print(search_bitonic_array([1, 3, 8, 12], 12))
    print(search_bitonic_array([10, 9, 8], 10))


main()
