'''
If there are more than one such triplet, return the sum of the triplet with the smallest sum

# Code Explain:
- Time complexity: O(n^2)
- Space complexity: O(n)

what we need to find is the "sum of closest pair", not the diff
so case [-3, -1, 1, 2], target=1
out: sum([-3, 1, 2])=0, not sum([-1, 1, 2])=2, through the gap is the same
i.e.: If there are more than one such triplet, return the sum of the triplet with the smallest sum

same as bp04
- target_sum is given
- we need to define a variable to describe `difference`: target_diff
- in bp04, we need to skip dulicate elements

need a function to find smallest_diff
- does the diff >0 or <0 matters?
  - actually abs(diff) is ok to find global minimul
  - >0 or <0 matters
'''


import math


def triplet_sum_close_to_target(arr, target_sum):
    arr.sort()
    smallest_diff = math.inf
    for i in range(len(arr) - 2):
        left = i + 1
        right = len(arr) - 1
        while (left < right):
            target_diff = target_sum - arr[i] - arr[left] - arr[right]
            if target_diff == 0:  # we've found a triplet with an exact sum
                return target_sum  # return sum of all the numbers

            # remember that our goal is to find a smallest_diff(global) close to 0
            # the second part of the following 'if' is to
            #   handle the smallest sum when we have more than one solution
            #   if simply using target_diff == -smallest_diff will include -1 +1 (t<s case)
            if abs(target_diff) < abs(smallest_diff) or \
                    (abs(target_diff) == abs(smallest_diff)
                        and target_diff > smallest_diff):
                smallest_diff = target_diff

            if target_diff > 0:
                left += 1  # we need a triplet with a bigger sum
            else:
                right -= 1  # we need a triplet with a smaller sum

    return target_sum - smallest_diff


def triplet_sum_close_to_target_v2(arr, target_sum):
    arr.sort()
    smallest_diff = math.inf
    for i in range(len(arr) - 2):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        # left = i + 1
        # in bp04, target_sum is 0
        smallest_diff = search_pair(arr, target_sum-arr[i], i + 1, smallest_diff)
        if smallest_diff == 0:
            return target_sum
    return target_sum - smallest_diff


def search_pair(arr, target_sum, left, smallest_diff):
    right = len(arr) - 1
    while (left < right):
        target_diff = target_sum - arr[left] - arr[right]
        if target_diff == 0:  # we've found a triplet with an exact sum
            return 0  # return smallest_diff

        # the second part of the following 'if' is to
        #   handle the smallest sum when we have more than one solution
        if abs(target_diff) < abs(smallest_diff) or \
                (abs(target_diff) == abs(smallest_diff)
                    and target_diff > smallest_diff):
            smallest_diff = target_diff

        if target_diff > 0:
            left += 1  # we need a triplet with a bigger sum
        else:
            right -= 1  # we need a triplet with a smaller sum
    return smallest_diff


def triplet_sum_close_to_target_my(arr, target_sum):
    def find_diff(target, subarr, smallest_diff):
        # !! find the one that has the abs(diff) closest to 0
        # since this is a sorted array, we can use two pointers to do that
        l = 0
        r = len(subarr) - 1
        while l < r:
            if l > 0 and subarr[l] == subarr[l - 1]:
                l += 1
            if r > 0 and subarr[r] == subarr[r - 1]:
                r -= 1
            diff = target - subarr[l] - subarr[r]
            if diff > 0:
                l += 1
            else:
                r -= 1

            # !! you cannnot simply use min(smallest_diff, diff)
            if abs(diff) < abs(smallest_diff) or \
                    (abs(diff) == abs(smallest_diff)
                        and diff > smallest_diff):
                smallest_diff = diff
        return smallest_diff

    arr.sort()
    smallest_diff = math.inf
    for i in range(len(arr) - 2):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        smallest_diff = find_diff(target_sum - arr[i], arr[i+1:], smallest_diff)

    return target_sum - smallest_diff  # target_sum - (target_sum - sum)


def main():
    print(triplet_sum_close_to_target([-2, 0, 1, 2], 2))
    # print(triplet_sum_close_to_target_v2([-2, 0, 1, 2], 2))
    print(triplet_sum_close_to_target([-3, -1, 1, 2], 1))
    # print(triplet_sum_close_to_target_v2([-3, -1, 1, 2], 1))
    # print(triplet_sum_close_to_target([1, 0, 1, 1], 100))


main()
