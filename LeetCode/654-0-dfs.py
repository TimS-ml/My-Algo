'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(N)

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def build(nums, lo, hi):
            # base case
            if lo > hi:
                return None

            # find index of maximum value
            # idx = nums.index(max(nums))
            idx = -1
            maxVal = -float('inf')
            for i in range(lo, hi+1):
                if maxVal < nums[i]:
                    idx = i
                    maxVal = nums[i]

            root = TreeNode(maxVal)
            root.left = build(nums, lo, idx-1)
            root.right = build(nums, idx+1, hi)
            return root

        return build(nums, 0, len(nums)-1)
