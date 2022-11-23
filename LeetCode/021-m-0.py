'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(1)

Feeback
- take care about edge cases
    - for examle, after while loop, will l1 or l2 remains?
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = list1, list2
        curr = ans = ListNode(0)

        # if using while p1.next and p2.next
        # then after while loop, p1 and p2 both remains
        while p1 and p2:
            if p1.val <= p2.val:
                curr.next = p1
                p1 = p1.next
                curr = curr.next
            else:
                curr.next = p2
                p2 = p2.next
                curr = curr.next
        if p1:
            curr.next = p1
        if p2:
            curr.next = p2
        return ans.next
