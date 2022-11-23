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
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(a, b):
            pre = None
            curr = a
            nxt = a
            while curr != b:
                nxt = curr.next  # buffer
                curr.next = pre  # change
                pre = curr  # move
                curr = nxt  # move
            return pre

        if not head:
            return None

        a = b = head

        # move to b to k
        for i in range(k):
            if b == None:
                return head
            b = b.next

        # reverse, and get new head
        newHead = reverse(a, b)

        # connect piece together
        a.next = self.reverseKGroup(b, k)

        return newHead
