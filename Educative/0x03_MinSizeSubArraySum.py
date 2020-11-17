# https://www.educative.io/courses/grokking-the-coding-interview/7XMlMEQPnnQ
# Given an array of positive numbers and a positive number ‘S’, find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0, if no such subarray exists.

# 2 pointers with un-fixed gap

import math
from collections import deque


# modifications:
# return subarr, not number
# gap is calculated based on S
def my(S, arr):
    start = 0
    minium = len(arr) + 1
    s = 0  # sum
    for end in range(len(arr)):
        s += arr[end]
        while s >= S:
            minium = min(minium, end - start + 1)  # don't forget to +1
            s -= arr[start]
            start += 1
    return minium


# deques
# if we need to return final subarrs
def my2(S, arr):
    start = 0
    minium = len(arr) + 1
    s = 0
    subarr = deque()
    for end in range(len(arr)):
        s += arr[end]
        subarr.append(arr[end])
        while s >= S:
            if end - start + 1 < minium:
                minium = end - start + 1
                ansarr = subarr
            s -= arr[start]
            subarr.popleft()
            start += 1
    return minium, ansarr


def smallest_subarray_with_given_sum(s, arr):
    window_sum = 0
    min_length = math.inf
    window_start = 0

    for window_end in range(0, len(arr)):
        window_sum += arr[window_end]  # add the next element
        # shrink the window as small as possible until the 'window_sum' is smaller than 's'
        while window_sum >= s:
            min_length = min(min_length, window_end - window_start + 1)
            window_sum -= arr[window_start]
            window_start += 1
    if min_length == math.inf:
        return 0
    return min_length


def main():
    print("Smallest subarray length: " + str(my(7, [2, 1, 5, 2, 3, 2])))

    print(str(my2(7, [2, 1, 5, 2, 3, 2])))

    # print("Smallest subarray length: " +
    #       str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))
    # print("Smallest subarray length: " +
    #       str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])))
    # print("Smallest subarray length: " +
    #       str(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))


main()
