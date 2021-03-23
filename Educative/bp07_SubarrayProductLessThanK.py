# time: O(n^3)  # why?
# they believe substr generation will cause n^2
# space: O(n^3)

# same as bp06
# this time we are calc sub arr product instead of sum
# **contiguous** subarrays, so don't sort arr

from collections import deque


def find_subarrays(arr, target):
    result = []
    product = 1  # can target=0 ? yes
    left = 0
    # at start, left and right are all 0
    for right in range(len(arr)):
        product *= arr[right]
        # why while loop ?
        # because l is `global`
        # in [2, 2, 5, 3, 10] case, when r at 10, l still at 5
        while (product >= target and left < len(arr)):
            # print(left, right, product)
            product /= arr[left]
            left += 1
        # since the product of all numbers from left to right is less than the target therefore,
        # all subarrays from left to right will have a product less than the target too; to avoid
        # duplicates, we will start with a subarray containing only arr[right] and then extend it
        temp_list = deque()
        # 2, 2, 5
        # r=2, l=0
        # order: [5], [2, 5], [2, 2, 5]
        # if not reverse: [2], [2, 2], [2, 2, 5]
        # we loop though r, and focus on right edges
        for i in range(right, left - 1, -1):
            temp_list.appendleft(arr[i])  # small number first
            result.append(list(temp_list))
            # print(right, left, temp_list, result)
    return result


def find_subarrays_v2(arr, target):
    result = []
    # at start, left and right are all 0
    for left in range(len(arr)):
        product = 1
        right = left
        while product < target and right < len(arr):
            product *= arr[right]
            right += 1
        if product >= target:
            right -= 1
        temp_list = []
        for i in range(left, right):
            temp_list.append(arr[i])
            result.append(list(temp_list))
            # print(right, left, temp_list, result)
    return result


def main():
    print(find_subarrays([2, 2, 5, 3, 10], 30))
    # print(find_subarrays_v2([2, 2, 5, 3, 10], 30))
    # print(find_subarrays([2, 2, 5, 3, 10], 0))
    # print(find_subarrays_v2([2, 2, 5, 3, 10], 0))
    # print(find_subarrays([8, 2, 6, 5], 50))


main()
