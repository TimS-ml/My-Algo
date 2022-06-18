'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

[A]
LCA = [1] start or dest
    = [2] node x, start at L, dest at R, or reverse

[B]
find path => 'LR' string
if [A.1], no overlap
if [A.2], overlap is: root to LCA

[C]
replace startPath with U
combine start and dest
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
class Solution {
    public String getDirections(TreeNode root, int startValue, int destValue) {
        this.startValue = startValue;
        this.destValue = destValue;
        // 寻找走到 startValue 和 destValue 的方向路径
        traverse(root);
        // 去除两个方向路径的公共前缀
        int p = 0, m = startPath.length(), n = destPath.length();
        while (p < m && p < n
                && startPath.charAt(p) == destPath.charAt(p)) {
            p++;
        }
        startPath = startPath.substring(p);
        destPath = destPath.substring(p);
        // 将走向 startValue 的方向路径全部变成 U
        startPath = "U".repeat(startPath.length());
        // 组合 startPath 和 destPath 就得到了答案
        return startPath + destPath;
    }

    StringBuilder path = new StringBuilder();
    String startPath, destPath;
    int startValue, destValue;

    // 二叉树遍历函数
    void traverse(TreeNode root) {
        if (root == null) {
            return;
        }
        if (root.val == startValue) {
            startPath = path.toString();
        } else if (root.val == destValue) {
            destPath = path.toString();
        }

        // 二叉树遍历框架
        path.append('L');
        traverse(root.left);
        path.deleteCharAt(path.length() - 1);

        path.append('R');
        traverse(root.right);
        path.deleteCharAt(path.length() - 1);
    }
}
'''
