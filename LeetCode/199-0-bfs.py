'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        
        next_level = deque([root,])
        rightside = []
        
        while next_level:
            # prepare for the next level
            curr_level = next_level
            next_level = deque()

            while curr_level:
                node = curr_level.popleft()
                    
                # add child nodes of the current level
                # in the queue for the next level
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            
            # The current level is finished.
            # Its last element is the rightmost one.
            rightside.append(node.val)
        
        return rightside
