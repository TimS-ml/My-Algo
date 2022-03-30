'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(1)

return nums.sort(key = lambda x: 1 if x == 0 else 0)
'''


class Solution:
    # fast slow pointers, same as lc 27
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        fast, slow = 0, 0
        while fast < len(nums):
            if nums[fast] != 0:
                # edge case, assign val to slow first
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        while slow < len(nums):
            nums[slow] = 0
            slow += 1
        return nums

    def moveZeroes_2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num_in = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums.insert(num_in, nums.pop(i))
                num_in += 1
        return nums


nums = [0, 1, 0, 3, 12]
print(Solution().moveZeroes(nums))
