'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

# Pros and Cons:
## Pros:

## Cons:

# Notation:

'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        curr = head
        i, j = head, head  # 2 swap points
        n = 1
        while curr:  # repeat length times
            if n < k:
                # l, i.next: k-1 times => kth element
                i = i.next
            if n > k:
                # r, j.next: length-k times => length-k+1 th element
                j = j.next
                curr = curr.next
            n += 1
        i.val, j.val = j.val, i.val
        return head
