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


# def find_sum_of_path_numbers(root):
#     return find_root_to_leaf_path_numbers(root, 0)

# def find_root_to_leaf_path_numbers(currentNode, pathSum):
#     if currentNode is None:
#         return 0

#     # calculate the path number of the current node
#     pathSum = 10 * pathSum + currentNode.val

#     # if the current node is a leaf, return the current path sum
#     if currentNode.left is None and currentNode.right is None:
#         return pathSum

#     # traverse the left and the right sub-tree
#     return find_root_to_leaf_path_numbers(currentNode.left, pathSum) + \
#            find_root_to_leaf_path_numbers(currentNode.right, pathSum)


def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))


main()
