'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

- All Node.val are unique
- p != q
- p and q exist in the tree
- Allow a node to be a descendant of itself
- We only know root p and q

LCA in persudo code without using `parent`, 
    based on the input `root` and p.val and q.val:
- loop through the answer node, we can find p and q
- keep in track of the looping route:
    - route x: a, b, ..., p
    - route y: a, b, ..., q
    - answer: the last intersection
    - stop once we find p or q

- case 1:
    - route x: a, b, c, .., p
    - route y: a, b, d, .., q
    - answer: the last intersection: b
- case 2:
    - route x: a, b, c, .., p
    - no q finded in dfs
    - answer: p

dfs

LCA in persudo code
    based on the input p and q:

- (you don't need this) dfs for p and q
- keep in track of their parents
'''

# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # # check if p or q is the LCA
        # # target should be p / q (node)
        # def dfs(node, target):
        #     if node:
        #         if node == target:
        #             return True
        #         dfs(node.left, target)
        #         dfs(node.right, target)
        #     return False

        # lca_check_p = dfs(p, q)
        # lca_check_q = dfs(q, p)

        # if lca_check_p:
        #     return p
        # elif lca_check_q:
        #     return q
        
        # since we know the node is unique
        path_p = set()  # set is a better answer than list

        while p:
            path_p.add(p)
            p = p.parent
        
        while q:
            if q in path_p:
                return q
            q = q.parent

    # O(1) space complexity
    # https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/discuss/932499/Simple-Python-Solution-with-O(1)-space-complexity
    def lowestCommonAncestor_2(self, p: 'Node', q: 'Node') -> 'Node':
        p1, p2 = p, q
        while p1 != p2:
            p1 = p1.parent if p1.parent else q
            p2 = p2.parent if p2.parent else p
            
        return p1

