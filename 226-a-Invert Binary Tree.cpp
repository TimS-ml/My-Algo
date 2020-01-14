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
    TreeNode* invertTree(TreeNode* root) {
        invert(root);
        return root;
        
    }
    void invertTree(TreeNode* root){
        if(root == NULL)
            return;
        TreeNode* temp = root->left;
        root->left = root->right;
        root->right = temp;
        invertTree(root->left);
        invertTree(root->right);
        return root;
    }
};

// class Solution {
// public:
//     TreeNode* invertTree(TreeNode* root) {
//         if(root == NULL)
//             return root;
//         TreeNode* temp = root->left;
//         root->left = root->right;
//         root->right = temp;
//         invertTree(root->left);
//         invertTree(root->right);
//         return root;
//     }
// };