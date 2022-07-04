'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # TLE for large k
    def rotateRight(self, head: Optional[ListNode],
                    k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head

        fast, slow = head, head
        for _ in range(k):
            if fast.next:
                fast = fast.next
            else:
                fast = head

        while fast.next:
            slow = slow.next
            fast = fast.next

        newHead = slow.next
        slow.next = None
        fast.next = head

        return newHead

