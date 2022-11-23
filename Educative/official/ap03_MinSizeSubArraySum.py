'''
https://www.educative.io/courses/grokking-the-coding-interview/7XMlMEQPnnQ

# Code Explain:
- Time complexity: O(N)
- Space complexity: O()

The outer for loop runs for all elements, and the inner while loop processes each element only once



Find the length of the smallest(len) contiguous subarray whose sum is greater than or equal to 'S'
case: 7, [2, 1, 5, 2, 3, 2]
[1] start = end, at arr[0]
[2] start at arr[0] not move, end at arr[2], sum > 7
[3] start at arr[1], end at arr[2] not move, sum < 7
[4] start at arr[1] not move, end at arr[3], sum > 7
...
'''


import math
from collections import deque


# 2 pointers with un-fixed gap
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
    ansarr = subarr = deque()
    for end in range(len(arr)):
        s += arr[end]
        subarr.append(arr[end])
        while s >= S:
            if end - start + 1 < minium:
                minium = end - start + 1
                ansarr = subarr
            s -= arr[start]
            subarr.popleft()  # yep, that's why I use deque
            start += 1
    return minium, ansarr


def smallest_subarray_with_given_sum(s, arr):
    window_sum = 0
    # min_length = math.inf
    min_length = len(arr) + 1  # I believe this is better
    window_start = 0

    for window_end in range(len(arr)):
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
