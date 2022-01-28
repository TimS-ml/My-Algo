'''
We are given an unsorted array containing ‘n+1’ numbers taken from the range 1 to ‘n’. 
The array has only one duplicate but it can be repeated multiple times. 
Find that duplicate number without using any extra space.

# Code Explain:
- Time complexity: O(N)
- Space complexity: O(1)

# Pros and Cons and Notation:

same as ep02
'''


def find_duplicate(nums):
    i = 0
    while i < len(nums):
        if nums[i] != i + 1:
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]  # swap
            else:  # we have found the duplicate
                return nums[i]
        else:
            i += 1

    return -1


def main():
    print(find_duplicate([1, 4, 4, 3, 2]))
    print(find_duplicate([2, 1, 3, 3, 5, 4]))
    print(find_duplicate([2, 4, 1, 4, 4]))


main()


# Can we solve the above problem in O(1) space and without modifying the input array?
# The array will have a cycle due to the duplicate number and that the start of the cycle will always point to the duplicate number
# This means that we can use the fast & the slow pointer
# The pointers jump between indexs

def find_duplicate_2(arr):
    slow, fast = arr[0], arr[arr[0]]
    while slow != fast:
        slow = arr[slow]
        fast = arr[arr[fast]]

    # find cycle length
    current = arr[arr[slow]]
    cycleLength = 1
    while current != arr[slow]:
        current = arr[current]
        cycleLength += 1

    return find_start(arr, cycleLength)


def find_start(arr, cycleLength):
    pointer1, pointer2 = arr[0], arr[0]
    # move pointer2 ahead 'cycleLength' steps
    while cycleLength > 0:
        pointer2 = arr[pointer2]
        cycleLength -= 1

    # increment both pointers until they meet at the start of the cycle
    while pointer1 != pointer2:
        pointer1 = arr[pointer1]
        pointer2 = arr[pointer2]

    return pointer1


def main_2():
    print(find_duplicate_2([1, 4, 4, 3, 2]))
    print(find_duplicate_2([2, 1, 3, 3, 5, 4]))
    print(find_duplicate_2([2, 4, 1, 4, 4]))


main_2()
