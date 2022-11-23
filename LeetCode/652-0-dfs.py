'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(N)

- How to compare:
    traverse result to str + hash dict
    only append once
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        ans = []
        dic = {}  # freq dict

        def dfs(node):
            if not node:
                return 'None'

            subL = dfs(node.left)
            subR = dfs(node.right)

            # post order
            subAll = subL + ',' + subR + ',' + str(node.val)

            freq = dic.get(subAll, 0)
            if freq == 1:  # only append once
                ans.append(node)

            dic[subAll] = dic.get(subAll, 0) + 1
            return subAll

        dfs(root)
        return ans

