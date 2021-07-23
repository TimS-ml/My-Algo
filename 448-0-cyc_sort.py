'''
# Code Explain:
- Time complexity: O(n)
- Space complexity: O(1)

# Pros and Cons and Notation:

'''

from typing import List


class Solution:
    def findDisappearedNumbers_cyc(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            # print('i:', i, nums)
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]  # swap
            else:
                # until nums[i] is in the correct position
                i += 1
        
        ans = []
        for i in range(len(nums)):
            if nums[i] != i+1:
                ans.append(i+1)
        return ans
    
    # hash table
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        l = len(nums)
        for n in nums:
            x = (n - 1) % l
            nums[x] += l
        
        return [i + 1 for i, num in enumerate(nums) if num <= l]


n = [4, 3, 2, 7, 8, 2, 3, 1]
print(Solution().findDisappearedNumbers(n))
