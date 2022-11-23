'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(N)

We cannot use in-order, can't deserialize

pre-order:
- se and dese are all pre-order
- since last root and lode list is like: x ['None', 'None', '']
    - so we will never loop to the last "''"

post-order:
- a little bit different in dese
- l.pop() will pop the last "''" as root, this is an edge case

Also, check 297-1, list operation is faster than string add
'''

from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec_pre_order:
    def serialize(self, root):
        """ Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        def helper(root):
            nonlocal s
            if not root:
                s = s + 'None' + ','
                return
            s = s + str(root.val) + ','
            helper(root.left)
            helper(root.right)

        s = ''
        helper(root)
        return s

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        """
        data: 1,2,None,None,3,4,None,None,5,None,None,
        1 ['2', 'None', 'None', '3', '4', 'None', 'None', '5', 'None', 'None', '']
        2 ['None', 'None', '3', '4', 'None', 'None', '5', 'None', 'None', '']
        3 ['4', 'None', 'None', '5', 'None', 'None', '']
        4 ['None', 'None', '5', 'None', 'None', '']
        5 ['None', 'None', '']
        """
        def deHelper(l):
            """ a recursive helper function for deserialization."""
            if not l:
                return None

            first = l.pop(0)
            if first == 'None':
                return None

            root = TreeNode(first)
            root.left = deHelper(l)
            root.right = deHelper(l)
            return root

        data_list = data.split(',')
        root = deHelper(data_list)
        return root


class Codec_post_order:
    def serialize(self, root):
        """ Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        def helper(root):
            nonlocal s
            if not root:
                s = s + 'None' + ','
                return
            helper(root.left)
            helper(root.right)
            s = s + str(root.val) + ','

        s = ''
        helper(root)
        return s

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        """
        data: None,None,2,None,None,4,None,None,5,3,1,
        1 ['None', 'None', '2', 'None', 'None', '4', 'None', 'None', '5', '3']
        3 ['None', 'None', '2', 'None', 'None', '4', 'None', 'None', '5']
        5 ['None', 'None', '2', 'None', 'None', '4', 'None', 'None']
        4 ['None', 'None', '2', 'None', 'None']
        2 ['None', 'None']
        """
        def deHelper(l):
            """ a recursive helper function for deserialization."""
            if not l:
                return None

            last = l.pop()
            if last == 'None':
                return None

            root = TreeNode(last)

            # !!! right node at top, so will run x.left first
            root.right = deHelper(l)
            root.left = deHelper(l)
            return root

        data_list = data.split(',')
        data_list.pop()  # [x, x, x, '']
        root = deHelper(data_list)
        return root


class Codec_level_order:
    def serialize(self, root):
        """ Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''

        s = ''
        q = deque([root])
        while q:
            node = q.popleft()

            if not node:
                s = s + 'None' + ','
                continue

            s = s + str(node.val) + ','
            q.append(node.left)
            q.append(node.right)

        return s

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        data_list = data.split(',')
        root = TreeNode(data_list[0])

        q = deque([root])
        i = 0
        while i < len(data_list) and q:
            node = q.popleft()

            i += 1
            left = data_list[i]
            if left != 'None':
                node.left = TreeNode(int(left))
                q.append(node.left)
            else:
                node.left = None

            i += 1
            right = data_list[i]
            if right != 'None':
                node.right = TreeNode(int(right))
                q.append(node.right)
            else:
                node.right = None

        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
