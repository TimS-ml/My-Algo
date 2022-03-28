'''
# need
- counter, x th = len - n

not get len, get nth
- fast: move n times
- slow

remove
- prev, curr


# case
n start with 1

[1] -> []

[1, 2] n=1 -> [1]

[1, 2] n=2 -> [2]

Feedback:
- nth from last!!!
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def getNode(head, n):
            fast, slow = head, head
            
            while n > 0:
                fast = fast.next
                n -= 1
            
            if fast:
                while fast.next:
                    fast  = fast.next
                    slow = slow.next
                return slow
            else:
                return None
            
        ans = head
        node = getNode(head, n)
        if not node:  # remove 1st node
            if ans.next:
                return ans.next
            else:
                return None
        
        if node.next.next:
            node.next = node.next.next
        else:
            node.next = None

        return ans
