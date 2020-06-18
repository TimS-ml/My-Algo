# https://leetcode-cn.com/problems/find-the-duplicate-number/
# this is faster


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for n in nums:
            if n in seen:
                return n
            seen.add(n)


nums = [1, 2, 2, 3, 4]
print(Solution().findDuplicate(nums))
