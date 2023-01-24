'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # you understand the question wrong!!!
    # def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
    #     dic = {}

    #     def dfs(node, lv):
    #         if str(lv) in dic:
    #             dic[str(lv)].append(node.val)
    #         else:
    #             dic[str(lv)] = [node.val]

    #         if node.left:
    #             dfs(node.left, lv + 1)
    #         if node.right:
    #             dfs(node.right, lv + 1)

    #     dfs(root, 0)
    #     print(dic)
