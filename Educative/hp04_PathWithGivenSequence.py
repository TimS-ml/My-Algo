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


def find_path(root, sequence):
    if not root:
        return len(sequence) == 0
    L = len(sequence)
    
    # pre-order?
    def dfs(currNode, idx):
        if currNode is None:
            return False

        if idx >= L or currNode.val != sequence[idx]:
            return False

        if currNode.left is None and currNode.right is None and idx == L - 1:
            return True

        return dfs(currNode.left, idx + 1) or dfs(currNode.right, idx + 1)

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
