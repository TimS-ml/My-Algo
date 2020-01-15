// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};


class Solution {
public:
    TreeNode* invertTree_recursive(TreeNode* root) {
        if (root == NULL) return root;
        TreeNode* node = invertTree_recursive(root->left);
        root->left = invertTree_recursive(root->right);
        root->right = node;
        return root;
    }
