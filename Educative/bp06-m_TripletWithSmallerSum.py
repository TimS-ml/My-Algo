'''
Count all triplets in it such that nums[i] + nums[j] + nums[k] < target where i, j, and k are three different indices

# Code Explain:
- Time complexity: O(n^2)
- Space complexity: O(n)

same as bp04
target_sum is given

since diff indices is ok (count all triplets), so do not skip duplicate

About that count += r-l:
    -1, 1, 3, 3, 4, 4 -> count += 5-1
idx  0  1  2  3  4, 5
    if 1, 4 matches the case (smaller than target_sum), 
        then number between l + 1 to r also matches
'''


def triplet_with_smaller_sum(nums, target_sum):
    def count_diff(idx, target):
        # !! find the one that has the abs(diff) closest to 0
        # since this is a sorted array, we can use two pointers to do that
        l = idx
        r = len(nums) - 1
        count = 0
        while l < r:
            # print(nums[l], nums[r])
            # target_sum - nums[i] - nums[l] - nums[r] > 0
            diff = target - nums[l] - nums[r]
            if diff > 0:
                # this is the edge cases
                # print(nums[l], nums[r])
                count += r - l
                l += 1
            else:
                r -= 1
        return count

    nums.sort()
    ans = 0
    for i in range(len(nums) - 2):
        ans += count_diff(i + 1, target_sum - nums[i])

    return ans


def main():
    # print(triplet_with_smaller_sum([-1, 0, 2, 3], 3))
    # print(triplet_with_smaller_sum([-1, -1, 4, 1], 5))
    # print(triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5))
    print(triplet_with_smaller_sum([-1, 1, 2, 3, 4], 5))


main()
