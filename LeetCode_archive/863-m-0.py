'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

case: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2

- locate the position of target
    def find():
        # [3, 5]
        return path of node

path reverse order of find() -> [5, 3]

- find in subtree (path[0])
    dfs(k, node=path[i])

- find in parents tree (path [1:])
    dfs(k - i, node=path[i])
        # make sure not search target branch ()
        if node.left != path[i+1]
        if node.right != path[i+1]

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        pass
