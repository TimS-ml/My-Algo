'''
# Code Explain:
- Time complexity: O(n^2)
- Space complexity: O(n)

return the sum of the triplet
'''

def triplet_sum_close_to_target(nums, target_sum):
    nums.sort()
    ans = float('inf')

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        target = target_sum - nums[i]
        start, end = i + 1, len(nums) - 1

        while start < end:
            target_diff = target_sum - (nums[start] + nums[end] + nums[i])
            if target_diff == 0:
                return target_sum

            if abs(target_diff) < abs(ans) or \
                    (abs(target_diff) == abs(ans)
                        and target_diff > ans):
                # print([nums[i], nums[start], nums[end])
                ans = target_diff

            if nums[start] + nums[end] > target:
                end -= 1
                while start < end and nums[end] == nums[end + 1]:
                    end -= 1
            elif nums[start] + nums[end] < target:
                start += 1
                while start < end and nums[start] == nums[start - 1]:
                    start += 1
    return target_sum - ans



def main():
    print(triplet_sum_close_to_target([-2, 0, 1, 2], 2))
    print(triplet_sum_close_to_target([-3, -1, 1, 2], 1))
    # print(triplet_sum_close_to_target([1, 0, 1, 1], 100))


main()
