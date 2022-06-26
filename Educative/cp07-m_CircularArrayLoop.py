'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(1)

'''


def circular_array_loop_exists(nums):
    L = len(nums)

    # need to go over all the elements
    for i in range(L):
        linkLength = 0
        j = i
        forward = nums[j] > 0
        while True:
            if (forward and nums[j] < 0) or (not forward and nums[j] > 0):
                break
            nextj = (j + nums[j] + L) % L
            # break until we found first one
            if nextj == j:
                break
            j = nextj
            linkLength += 1
            if linkLength > L:
                return True
    return False


def main():
    print(circular_array_loop_exists([1, 2, -1, 2, 2]))
    print(circular_array_loop_exists([2, 2, -1, 2]))
    print(circular_array_loop_exists([2, 1, -1, -2]))


main()
