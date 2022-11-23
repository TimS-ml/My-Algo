'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()


Feedback:
- You should remove common ancestors during recursion


[A]
LCA = [1] start or dest
    = [2] node x, start at L/R, dest at R/L

[B]
find path => 'LRU' string

[C] concat
reverse: replace all L/R to U

[1] [1.1] if LCA = start => return
    [1.2] if LCA = dest => return reverse
[2] reverse (LCA -> start) + (LCA -> dest)
'''

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def rev(path):
            path = path.replace('L', 'U')
            path = path.replace('R', 'U')
            return path

        def helper(node, path):
            if not node:
                return None
            elif node.val == startValue:
                return path
            elif node.val == destValue:
                return path

            subL = helper(node.left, 'L')
            subR = helper(node.right, 'R')

            # A.2
            if subL and subR:
                # LCA is node => C.2
                # find start L or R ???

                return

            # A.1
            elif subL:
                # C.1
                # determine LCA = start or dest
                return subL

            # A.1
            elif subR:
                # C.1
                # determine LCA = start or dest
                return subR

        return helper(root, '')

