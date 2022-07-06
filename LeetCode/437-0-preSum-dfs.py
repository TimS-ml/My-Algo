'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(N)

'''

from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # You don't need to save prefix targetSum seqence !!!
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        def dfs(node, pathSumCurr) -> None:
            nonlocal count
            if not node:
                return 
            
            # current prefix targetSum
            pathSumCurr += node.val
            
            # here is the targetSum we're looking for
            if pathSumCurr == targetSum:
                count += 1
            
            # the state is the feq dict!!!
            # number of times the pathSumCurr − targetSum has occurred already, 
            # determines the number of times a path with targetSum targetSum 
            # has occurred up to the current node
            count += dic[pathSumCurr - targetSum]
            
            # add the current targetSum into hashmap
            # to use it during the child nodes processing
            dic[pathSumCurr] += 1
            
            # process left subtree
            dfs(node.left, pathSumCurr)
            # process right subtree
            dfs(node.right, pathSumCurr)
            
            # backtrack
            # remove the current targetSum from the hashmap
            # in order not to use it during 
            # the parallel subtree processing
            dic[pathSumCurr] -= 1
            
        count = 0
        dic = defaultdict(int)
        dfs(root, 0)
        return count


    # without pathSumCurr
    def pathSum_2(self, root: TreeNode, targetSum: int) -> int:
        count = 0
        pathSumCurr = 0
        dic = defaultdict(int)  # count dict
        dic[0] = 1

        def dfs(node):
            if not node:
                return

            nonlocal count, pathSumCurr

            # pre-order
            pathSumCurr += node.val
            count += dic[pathSumCurr - targetSum]
            dic[pathSumCurr] += 1

            dfs(node.left)
            dfs(node.right)

            # post-order
            dic[pathSumCurr] -= 1
            pathSumCurr -= node.val

        dfs(root)
        return count
