'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(N)

'''


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# check lc 437
def count_paths(root, S):
    pass


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(11)  # sub-path in middle counts
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has paths: " + str(count_paths(root, 11)))


main()
