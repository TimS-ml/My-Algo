'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''
from collections import deque

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        queue = deque([root,])
        rightside = []

        while queue:
            # prepare for the next level
            curr_level = queue
            queue = deque()

            while curr_level:
                node = curr_level.popleft()

                # add child nodes of the current level
                # in the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # The current level is finished.
            # Its last element is the rightmost one.
            rightside.append(node.val)

        return rightside
