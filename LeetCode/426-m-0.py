'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

Feedback:
You are not fully understand the question, what we really want is:
    l.end <-> node <-> r.start
    in-order to a special list

In place: no return please
'''

class Solution:
    # failed on only right tree case
    def treeToDoublyList_raw(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def helper(node):
            l = helper(node.left) if node.left else None
            r = helper(node.right) if node.right else None

            if l:
                node.left = l
                l.right = node
            else:
                node.left = None

            if r:
                node.right = r
                r.left = node
            else:
                node.right = None

            # end of list
            if node.right:
                return node.right
            else:
                return node

        if not root:
            return None

        start = root

        while start.left:
            start = start.left

        end = helper(root)

        # connect first and last node
        start.left = end
        end.right = start

        return start
