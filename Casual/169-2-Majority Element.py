# https://leetcode-cn.com/problems/majority-element/


class Solution:
    def majorityElement(self, nums) -> int:
        count = 1
        maj = nums[0]
        for i in range(1, len(nums)):
            if maj == nums[i]:
                count += 1
            else:
                count -= 1
                # count=0的时候，前面的数肯定被对掉了，剩下频率最高的数
                if count == 0:
                    maj = nums[i + 1]
        return maj


input_nums = [3, 2, 2, 2, 3, 3, 3]
print(Solution().majorityElement(input_nums))
