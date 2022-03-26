'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(N)

Case:
Two trees that matches the same pre / post order
Tree1
1
  2
    3

Tree2
    1 
  2
3
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        postorder_idx_map = {val: idx for idx, val in enumerate(postorder)}

        def build(preStart, preEnd, postStart, postEnd):
            if preStart > preEnd:
                return None
            
            if preStart == preEnd:
                return TreeNode(preorder[preStart])

            rootVal = preorder[preStart]

            leftRootVal = preorder[preStart + 1]

            # find in post-order in range(inStart, inEnd)
            # be aware of this edge case
            idx = postorder_idx_map[leftRootVal]

            leftSize = idx - postStart + 1

            root = TreeNode(rootVal)
            # idx = leftSize + postStart - 1
            root.left = build(preStart + 1, preStart + leftSize,
                              postStart, postStart + leftSize - 1)
            root.right = build(preStart + leftSize + 1, preEnd,
                               postStart + leftSize, postEnd - 1)
            return root

        return build(0, len(preorder)-1, 
                     0, len(postorder)-1)
