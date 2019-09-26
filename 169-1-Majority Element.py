# https://leetcode-cn.com/problems/majority-element/
# The majority element is the element that appears more than ⌊ n/2 ⌋ times.


class Solution:
    def majorityElement(self, nums) -> int:
        # 取sorted的list的中间
        return sorted(nums)[int(len(nums)/2)]


input_nums = [3, 2, 3]
print(Solution().majorityElement(input_nums))
