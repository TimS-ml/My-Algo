'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(N)

Backtrack + cut leaf
'''

# from collections import deque

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# You don't need to modify the seq, compare val at idx is ok
def find_path(root, sequence):

    def dfs(node, idx):
        if not node:
            return idx == len(sequence)

        if sequence[idx] != node.val:
            return False

        l = dfs(node.left, idx + 1)
        r = dfs(node.right, idx + 1)
        return l or r
        
    return dfs(root, 0)


def main():

    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)

    print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
    print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))


main()
