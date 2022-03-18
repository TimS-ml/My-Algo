'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(1)

Feedback:
- start point!!!
- You know we have 2 situations: 1 mid (odd) or 2 mid (even)
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # slow, fast = ListNode(0), ListNode(0)
        # slow.next, fast.next = head, head
        slow, fast = head, head
        while fast.next:
            slow = slow.next
            fast = fast.next
            if fast.next:
                fast = fast.next
            else:
                return slow
        return slow
