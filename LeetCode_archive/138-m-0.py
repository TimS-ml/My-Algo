'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dic = {}

        def helper(node):
            if not node:
                return None

            if node in dic:
                return dic[node]

            newNode = Node(node.val, None, None)
            dic[node] = newNode  # !!!

            newNode.next = helper(node.next)
            newNode.random = helper(node.random)

            return newNode

        return helper(head)
