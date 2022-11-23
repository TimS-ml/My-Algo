'''
We are given an array containing 'n' objects.
Each object, when created, was assigned a unique number from 1 to 'n' based on their creation sequence.
This means that the object with sequence number '3' was created just before the object with sequence number '4'.

# Code Explain:
- Time complexity: O(N)
- Space complexity: O(1)



i: 0 [2, 4, 5, 1, 3]
i: 0 [4, 2, 5, 1, 3]
i: 0 [1, 2, 5, 4, 3]
i: 1 [1, 2, 5, 4, 3] do nothing
i: 2 [1, 2, 5, 4, 3]
i: 2 [1, 2, 3, 4, 5]
i: 3 [1, 2, 3, 4, 5] do nothing
i: 4 [1, 2, 3, 4, 5] do nothing
'''

def cyclic_sort(nums):
    i = 0
    while i < len(nums):
        print('i:', i, nums)
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]  # swap
        else:
            # until nums[i] is in the correct position
            i += 1
    return nums


def main():
    print(cyclic_sort([2, 4, 5, 1, 3]))
    # print(cyclic_sort([3, 1, 5, 4, 2]))
    # print(cyclic_sort([2, 6, 4, 3, 1, 5]))
    # print(cyclic_sort([1, 5, 6, 4, 3, 2]))


main()
