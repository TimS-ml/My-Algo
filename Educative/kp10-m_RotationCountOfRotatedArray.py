'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

lc 153
'''


# this return val not idx
def count_rotations(nums):
    ans = nums[0]
    l, r = 0, len(nums) - 1

    while l <= r:
        if nums[l] < nums[r]:
            ans = min(ans, nums[l])
            break

        m = (l + r) // 2
        ans = min(ans, nums[m])
        if nums[m] >= nums[l]:
            l = m + 1
        else:
            r = m - 1
    return ans


def main():
    print(count_rotations([10, 15, 1, 3, 8]))
    print(count_rotations([4, 5, 7, 9, 10, -1, 2]))
    print(count_rotations([1, 3, 8, 10]))


main()
