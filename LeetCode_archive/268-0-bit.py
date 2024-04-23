'''
# Code Explain:
sol 1
- Time complexity: O(n)
- Space complexity: O(1)

sum(nums) may be very big
'''


class Solution:
    # sum: O(n) time
    def missingNumber(self, nums) -> int:
        n = len(nums)
        # (n * (n + 1)) / 2 = 1 + 2 + ... x + ... + n
        # sum(nums)         = 1 + 2 + ... 0 + ... + n
        return int((n * (n + 1)) / 2 - sum(nums))

    def missingNumber_2(self, nums) -> int:
        nums_set = set(nums)  # kind like hash

        for i in range(len(nums)):
            if i not in nums_set:
                return i
        else:
            return len(nums)

    # bit XOR
    # a ^ a = 0
    def missingNumber_3(self, nums):
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing


# nums = [3, 0, 1]  # 2
nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]  # 8
print(Solution().missingNumber_2(nums))
