'''
Count all triplets in it such that arr[i] + arr[j] + arr[k] < target where i, j, and k are three different indices

# Code Explain:
- Time complexity: O(n^2)
- Space complexity: O(n)

# Pros and Cons and Notation:

same as bp04
target_sum is given
we need to define a similar var: target_diff
!! differnet indices counts
  which means we allow duplicates

About that count += r-l:
-1, 1, 4 -> count += 3 (4-1)
    since if 1, 4 matches the case, then 1, 3 / 1, 2 also matches
    so, count += from arr[l] to all numbers<=arr[r]
-1, 2, 3

Generally speaking, find all (a, b) that a+b<c
'''


def triplet_with_smaller_sum(arr, target):
    arr.sort()
    count = 0
    for i in range(len(arr) - 2):
        # if i > 0 and arr[i] == arr[i - 1]:
        #     continue
        count += search_pair(arr, i + 1, target - arr[i])
    return count


def search_pair(arr, left, target_sum):
    count = 0
    right = len(arr) - 1
    while (left < right):
        if arr[left] + arr[right] < target_sum:  # found the triplet
            # since arr[right] >= arr[left], therefore, we can replace arr[right] by any number between
            # left and right to get a sum less than the target sum
            # !!! this is smart !!!
            count += right - left
            left += 1
        else:
            right -= 1  # we need a pair with a smaller sum
    return count


# if return triplet, not return count
def triplet_with_smaller_sum_t(arr, target):
    arr.sort()
    triplets = []
    for i in range(len(arr) - 2):
        # if i > 0 and arr[i] == arr[i - 1]:
        #     continue
        search_pair_t(arr, i + 1, target - arr[i], triplets)
    return triplets


def search_pair_t(arr, left, target_sum, triplets):
    for i in range(left, len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] < target_sum:
                triplets.append([arr[left - 1], arr[left], arr[i]])


def main():
    # print(triplet_with_smaller_sum([-1, 0, 2, 3], 3))
    # print(triplet_with_smaller_sum([-1, -1, 4, 1], 5))
    # print(triplet_with_smaller_sum_t([-1, -1, 4, 1], 5))
    print(triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5))
    print(triplet_with_smaller_sum_t([-1, 4, 2, 1, 3], 5))


main()
