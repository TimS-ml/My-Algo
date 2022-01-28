'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(N)

# Pros and Cons and Notation:

'''


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_sum_of_path_numbers(root):
    def dfs(currNode, s):
        if not currNode:
            return 0
        s = 10 * s + currNode.val

        # leaf
        if currNode.left is None and currNode.right is None:
            return s

        return dfs(currNode.left, s) + dfs(currNode.right, s)

    return dfs(root, 0)


def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))


main()
