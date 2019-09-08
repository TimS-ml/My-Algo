# https://leetcode-cn.com/problems/binary-tree-longest-consecutive-sequence-ii/



class Solution(object):
    def longestConsecutive(self, root):
        def dfs(root):
            if not root:
                return None, 0, 0, 0    # increasing length, decreasing length, global max length
            inc = dec = 1
            left, leftInc, leftDec, leftMax = dfs(root.left)
            right, rightInc, rightDec, rightMax = dfs(root.right)
            if root.val + 1 == left:
                inc = max(leftInc + 1, inc)
            if root.val - 1 == left:
                dec = max(leftDec + 1, dec)
            if root.val + 1 == right:
                inc = max(rightInc + 1, inc)
            if root.val - 1 == right:
                dec = max(rightDec + 1, dec)
            return root.val, inc, dec, max(inc + dec - 1, leftMax, rightMax, inc, dec)

        return dfs(root)[3]
