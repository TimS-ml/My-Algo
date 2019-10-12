# https://leetcode-cn.com/problems/3sum/


class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()
        # order: i < j < k
        # nums: i <= j <= k
        for i in range(len(nums)-2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j, k = i+1, len(nums)-1
            while j < k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                else:
                    res.append((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
        return res


nums = [-1, 0, 1, 2, -1, -4]  # [(-1, -1, 2), (-1, 0, 1)]
nums2 = [-4, -1, -1, 0, 1, 2]
nums3 = [0, 0, 0, 0]
nums4 = [-2, 0, 1, 1, 2]  # [[-2, 0, 2],[-2, 1, 1]]

print(Solution().threeSum(nums4))
