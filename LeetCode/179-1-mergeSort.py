'''
# Code Explain:
- Time complexity: O(N logN)
- Space complexity: O(n)

'''
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = self.mergeSort(nums, 0, len(nums)-1)
        return str(int("".join(map(str, nums))))

    # input: int
    def compare(self, n1, n2):
        # both > or >= is ok
        return str(n1) + str(n2) >= str(n2) + str(n1)
    
    # this is same as normal merge sort
    def mergeSort(self, nums, l, r):
        if l > r:
            return 
        if l == r:
            return [nums[l]]
        mid = l + (r-l)//2
        left = self.mergeSort(nums, l, mid)
        right = self.mergeSort(nums, mid+1, r)
        return self.merge(left, right)
        
    # specifiy compare rules
    def merge(self, l1, l2):
        ans, i, j = [], 0, 0
        while i < len(l1) and j < len(l2):
            if not self.compare(l1[i], l2[j]):
                ans.append(l2[j])
                j += 1
            else:
                ans.append(l1[i])
                i += 1
        ans.extend(l1[i:] or l2[j:])
        return ans


nums = [3, 30, 34, 5, 9]
print(Solution().largestNumber(nums))
