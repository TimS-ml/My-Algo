'''
stack of l1 and l2
- get the length of l1 and l2
    - align l1 and l2
- carry + reminder => divmod
- 2 pointers for each linked list: curr and prev

- calculate final result
- reverse linked list (or create a linked list in reverse order directly)
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1, s2 = [], []
        
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        
        carry, head = 0, None

        while s1 or s2 or carry:
            d1, d2 = 0, 0
            d1 = s1.pop() if s1 else 0
            d2 = s2.pop() if s2 else 0
            carry, digit = divmod(d1 + d2 + carry, 10)
            head_new = ListNode(digit)
            head_new.next = head
            head = head_new
            
        return head
