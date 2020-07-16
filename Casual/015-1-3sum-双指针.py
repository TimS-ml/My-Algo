# https://leetcode-cn.com/problems/3sum/


class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()
        # 这里面有3个指针，i start end
        # nums[start] + nums[end] = target = 0 - nums[i]
        for i in range(0, len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:  # 避免重复计算
                continue
            target = 0 - nums[i]
            start, end = i + 1, len(nums) - 1
            while start < end:
                # 从两侧逼近
                if nums[start] + nums[end] > target:
                    end -= 1
                elif nums[start] + nums[end] < target:
                    start += 1
                else:
                    # print(nums[i], nums[start], nums[end])
                    res.append((nums[i], nums[start], nums[end]))
                    end -= 1
                    start += 1
                    while start < end and nums[end] == nums[end + 1]:
                        end -= 1
                    while start < end and nums[start] == nums[start - 1]:
                        start += 1
        return res


# [-4, -1, -1, 0, 1, 2]
nums = [-1, 0, 1, 2, -1, -4]
print(Solution().threeSum(nums))
