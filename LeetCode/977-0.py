'''
# Code Explain:
sol 1
- Time complexity: O(NlongN)
- Space complexity: O(longN)

sol 2
- Time complexity: O(N)
- Space complexity: O(1)

- find boundary of <0 and >=0
- two pointers from middle to edge
'''

from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums = [n**2 for n in nums]
        return sorted(nums)

    def sortedSquares_2(self, nums: List[int]) -> List[int]:
        L = len(nums)
        neg = -1  # init negative value location
        for k, v in enumerate(nums):
            if v < 0:
                neg = k
            else:
                break

        ans = []
        l, r = neg, neg + 1

        while l >= 0 or r < L:
            if l < 0:  # move r
                ans.append(nums[r]**2)
                r += 1
            elif r == L:  # move l
                ans.append(nums[l]**2)
                l -= 1
            else:
                if nums[l]**2 < nums[r]**2:
                    ans.append(nums[l]**2)
                    l -= 1
                else:
                    ans.append(nums[r]**2)
                    r += 1
        return ans
