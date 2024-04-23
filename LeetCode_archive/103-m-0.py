'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

modified the level order trivsal
'''

from typing import List, Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        # reverse = False
        q = deque()
        q.append([root, 0])  # node and it's level
        dic = {}

        while q:
            node, lv = q.popleft()
            if node:
                # ok this line is buggy
                dic[str(lv)] = dic.get(str(lv), []).append(node.val)
                q.append([node.left, lv + 1])
                q.append([node.right, lv + 1])
        
        for k, v in dic:
            if int(k) % 2 == 0:
                ans.extend(v)
            else:
                ans.extend(v[::-1])
            
        return ans
