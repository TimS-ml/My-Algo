'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''

class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        node = Node(insertVal)

        if not head:
            node.next = node
            return node

        prev, curr = head, head.next

        while prev.next != head:
            # Case1:
            # 1 <- Node(2) <- 3
            # prev < curr
            if prev.val <= node.val <= curr.val:
                break

            # Case2 and 3: beginning and end of loop
            # 3 -> 1, 3 -> Node(4) -> 1
            if prev.val > curr.val and node.val > prev.val:
                break

            # 3 -> 1, 3 -> Node(0) -> 1
            if prev.val > curr.val and node.val < curr.val:
                break

            prev, curr = prev.next, curr.next

        # Insert node.
        node.next = curr
        prev.next = node

        return head
