'''
# Code Explain:
- Time complexity: O(n^2)
- Space complexity: O(n)

# Pros and Cons and Notation:

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
    print(triplet_sum_close_to_target([-3, -1, 1, 2], 1))
    # print(triplet_sum_close_to_target([1, 0, 1, 1], 100))


main()
