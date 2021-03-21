# time: O(n^2)
# space: O(n)

# same as bp04
# target_sum is given
# we need to define a similar var: target_diff
# in bp04, we need to skip dulicate elements
# case: [-1, -1, -1, 2], 1

import math


def triplet_sum_close_to_target(arr, target_sum):
    arr.sort()
    smallest_difference = math.inf
    for i in range(len(arr) - 2):
        left = i + 1
        right = len(arr) - 1
        while (left < right):
            target_diff = target_sum - arr[i] - arr[left] - arr[right]
            if target_diff == 0:  # we've found a triplet with an exact sum
                return target_sum  # return sum of all the numbers

            # the second part of the following 'if' is to handle the smallest sum when we have more than one solution
            if abs(target_diff) < abs(smallest_difference) or (
                    abs(target_diff) == abs(smallest_difference)
                    and target_diff > smallest_difference):
                smallest_difference = target_diff  # save the closest and the biggest difference

            if target_diff > 0:
                left += 1  # we need a triplet with a bigger sum
            else:
                right -= 1  # we need a triplet with a smaller sum

    return target_sum - smallest_difference


def triplet_sum_close_to_target_v2(arr, target_sum):
    arr.sort()
    # triplets = []  # we don't need to save this
    smallest_difference = math.inf
    for i in range(len(arr) - 2):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        # left = i + 1
        # in bp04, target_sum is 0
        smallest_difference = search_pair(arr, target_sum-arr[i], i + 1, smallest_difference)
        if smallest_difference == 0:
            return target_sum
    return target_sum - smallest_difference


def search_pair(arr, target_sum, left, smallest_difference):
    right = len(arr) - 1
    while (left < right):
        target_diff = target_sum - arr[left] - arr[right]
        if target_diff == 0:  # we've found a triplet with an exact sum
            return 0  # return smallest_difference

        # the second part of the following 'if' is to handle the smallest sum when we have more than one solution
        if abs(target_diff) < abs(smallest_difference) or (
                abs(target_diff) == abs(smallest_difference)
                and target_diff > smallest_difference):
            smallest_difference = target_diff  # save the closest and the biggest difference

        if target_diff > 0:
            left += 1  # we need a triplet with a bigger sum
        else:
            right -= 1  # we need a triplet with a smaller sum
    return smallest_difference


def main():
    # print(triplet_sum_close_to_target([-2, 0, 1, 2], 2))
    # print(triplet_sum_close_to_target_v2([-2, 0, 1, 2], 2))
    print(triplet_sum_close_to_target([-3, -1, 1, 2], 1))
    print(triplet_sum_close_to_target_v2([-3, -1, 1, 2], 1))
    # print(triplet_sum_close_to_target([1, 0, 1, 1], 100))


main()
