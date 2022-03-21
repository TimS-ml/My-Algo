'''
# Code Explain:
- Time complexity: O(N logN)
- Space complexity: O(n)

'''
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        self.quickSort(nums, 0, len(nums)-1)
        return str(int("".join(map(str, nums)))) 

    # input: int
    def compare(self, n1, n2):
        # this is >=, otherwise this will leads to wrong behavior in swap
        return str(n1) + str(n2) >= str(n2) + str(n1)

    def quickSort(self, nums, l, r):
        if l >= r:
            return 

        p = self.partition(nums, l, r)
        self.quickSort(nums, l, p-1)
        self.quickSort(nums, p+1, r)
        
    # def partition(self, nums, l, r):
    #     low = l
    #     while l < r:
    #         if self.compare(nums[l], nums[r]):
    #             nums[l], nums[low] = nums[low], nums[l]
    #             low += 1
    #         l += 1
    #     nums[low], nums[r] = nums[r], nums[low]
    #     return low

    # from my template
    def partition(self, nums, l, r):
        pivot_idx = l
        pivot = nums[pivot_idx]

        while l < r:
            while l < len(nums) and self.compare(nums[l], pivot):
                l += 1
            while not self.compare(nums[r], pivot):
                r -= 1
            if l < r:
                nums[l], nums[r] = nums[r], nums[l]
        nums[r], nums[pivot_idx] = nums[pivot_idx], nums[r]
        return r


nums = [3, 30, 34, 5, 9]  # 9534330
print(Solution().largestNumber(nums))
