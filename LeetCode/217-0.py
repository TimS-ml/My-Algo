'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(1)

simply len(nums) != len(set(nums))
hash set solution costs O(N) space complexity!!!

'''


class Solution:
    def containsDuplicate(self, nums) -> bool:
        # for i in range(len(nums)):
        #     if nums.index(nums[i]) != i:
        #         return True
        # return False

        if len(nums) == 0 or len(nums) == 1:
            return False

        for i in range(len(nums) - 1, 0, -1):
            if nums.index(nums[i]) != i:
                return True
        return False

    # sort is slow
    def containsDuplicate_2(self, nums) -> bool:
        nums.sort()
        i = 1
        while i < len(nums):
            if nums[i-1] ^ nums[i] == 0: 
                return True 
            i += 1
        return False


nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
print(Solution().containsDuplicate(nums))
