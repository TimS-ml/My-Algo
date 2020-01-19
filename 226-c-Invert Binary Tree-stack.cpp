/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
  TreeNode *invertTree_non_recursive(TreeNode *root) {
    if (root == NULL)
      return root;
    vector<TreeNode *> stack;
    stack.push_back(root);
    while (!stack.empty()) {
      TreeNode *node = stack.back();
      stack.pop_back();
      swap(node->left, node->right);
      if (node->left)
        stack.push_back(node->left);
      if (node->right)
        stack.push_back(node->right);
    }
    return root;
  }
