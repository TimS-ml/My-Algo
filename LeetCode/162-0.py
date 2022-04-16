'''
# Code Explain:
- Time complexity: O(logN)
- Space complexity: O(1)

https://leetcode.com/problems/find-peak-element/discuss/1290642/Intuition-behind-conditions-or-Complete-Explanation-or-Diagram-or-Binary-Search
https://leetcode.com/problems/find-peak-element/discuss/50259/My-clean-and-readable-python-solution

edge case:
[1, 2, 3] => '3' are the peak (idx -1)
[3, 2, 1] => '3' are the peak (idx 1)
'''

class Solution:
    # Iterative Binary Search
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1

        while left < right-1:
            mid = left + (right-left)//2
            # target
            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                return mid
                
            # change search space
            if nums[mid] < nums[mid+1]:
                left = mid+1
            else:
                right = mid-1
                
        # after while loop: left = right - 1
        if nums[left] >= nums[right]:
            return left
        else:
            return right
