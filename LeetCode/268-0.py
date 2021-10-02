'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

# Pros and Cons and Notation:
sum(nums) may be very big
'''


class Solution:
    def missingNumber(self, nums) -> int:
        n = len(nums)
        return int((n * (n + 1)) / 2 - sum(nums))

    def missingNumber_2(self, nums) -> int:
        nums_set = set(nums)

        for i in range(len(nums)):
            if i not in nums_set:
                return i
        else:
            return len(nums)


# nums = [3, 0, 1]  # 2
nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]  # 8
print(Solution().missingNumber_2(nums))
