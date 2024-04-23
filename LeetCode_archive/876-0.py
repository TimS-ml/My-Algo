'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(1)
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    # in this case time and space are both O(N)
    def middleNode_2(self, head: ListNode) -> ListNode:
        nodes = [head]
        # append all nodes to a list
        while nodes[-1].next:
            nodes.append(nodes[-1].next)
        return nodes[len(nodes) // 2]
