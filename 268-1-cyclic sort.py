'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

# Pros and Cons and Notation:

'''


class Solution(object):
    def missingNumber(self, nums):
        i = 0
        while i < len(nums):
            expected_index = nums[i]
            if expected_index != i and expected_index < len(nums):
                nums[expected_index], nums[i] = nums[i], nums[expected_index]
            else:
                i += 1
                
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        
        return len(nums)


# nums = [3, 0, 1]  # 2
nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]  # 8
print(Solution().missingNumber(nums))
