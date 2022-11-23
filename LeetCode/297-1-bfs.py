'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''

from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize_str(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''

        s = ''
        q = deque([root])

        while q:
            curr = q.popleft()

            if not curr:
                s = s + 'None' + ','
                continue

            s = s + str(curr.val) + ','

            q.append(curr.left)
            q.append(curr.right)

        return s

    # list operation is faster than string add
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''

        s = []
        q = deque([root])

        while q:
            curr = q.popleft()

            if not curr:
                s.append('None')
                continue

            s.append(str(curr.val))

            q.append(curr.left)
            q.append(curr.right)

        return ','.join(s)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return []

        data_list = data.split(',')
        root = TreeNode(data_list[0])
        q = deque([root])

        i = 0
        while q:
            parent = q.popleft()

            i += 1
            left = data_list[i]
            if left != 'None':
                parent.left = TreeNode(left)
                q.append(parent.left)
            else:
                parent.left = None

            i += 1
            right = data_list[i]
            if right != 'None':
                parent.right = TreeNode(right)
                q.append(parent.right)
            else:
                parent.right = None

        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
