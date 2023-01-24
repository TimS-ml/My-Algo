'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''

from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # using a clever way to tag level
    # [node1, None, node1.l, node1.r, None ...]
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        level_list = deque()
        if root is None:
            return []

        # start with the level 0 with a delimiter
        node_queue = deque([root, None])
        order_left = True

        while len(node_queue) > 0:
            curr_node = node_queue.popleft()

            if curr_node:
                if order_left:
                    level_list.append(curr_node.val)
                else:
                    level_list.appendleft(curr_node.val)

                if curr_node.left:
                    node_queue.append(curr_node.left)
                if curr_node.right:
                    node_queue.append(curr_node.right)
            else:
                # we finish one level
                ans.append(level_list)
                # add a delimiter to mark the level
                if len(node_queue) > 0:
                    node_queue.append(None)

                # prepare for the next level
                level_list = deque()
                order_left = not order_left

        return ans

    # yet another way to track the lengh of each level
    def zigzagLevelOrder_2(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        level_list = deque()
        if root is None:
            return []

        node_queue = deque([root])
        order_left = True

        while len(node_queue) > 0:
            level_len = len(node_queue)
            for _ in range(level_len):
                curr_node = node_queue.popleft()
                if order_left:
                    level_list.append(curr_node.val)
                else:
                    level_list.appendleft(curr_node.val)

                if curr_node.left:
                    node_queue.append(curr_node.left)
                if curr_node.right:
                    node_queue.append(curr_node.right)

            # we finish one level
            ans.append(level_list)

            # prepare for the next level
            level_list = deque()
            order_left = not order_left

        return ans
