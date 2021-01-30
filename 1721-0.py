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
        n = 0
        # n: get length of ListNode
        while curr:
            curr = curr.next
            n += 1
        i, j = k, n - k + 1  # 2 swap points

        # get the value at i and j
        n = ai = aj = 0
        curr = head
        while curr:
            n += 1
            if n == i: ai = curr.val
            if n == j: aj = curr.val
            curr = curr.next

        # replace the value
        n = 0
        curr = head
        while curr:
            n += 1
            if n == i: curr.val = aj
            if n == j: curr.val = ai
            curr = curr.next

        return head
