'''
# Code Explain:
- Time complexity: O(N)

Need backtrack
'''


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_paths(root, required_sum):
    ans = []

    def dfs(node, s, path):
        nonlocal ans
        if not node.left and not node.right and s == node.val:
            ans.append(path + [node.val])

        if node.left:
            dfs(node.left, s - node.val, path + [node.val])
        if node.right:
            dfs(node.right, s - node.val, path + [node.val])

    dfs(root, required_sum, [])
    return ans


def main():

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    required_sum = 23
    print("Tree paths with required_sum " + str(required_sum) + ": " +
          str(find_paths(root, required_sum)))


main()
