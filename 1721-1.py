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
        i, j = head, head # 2 swap points
        n = 1
        while curr:
            if n < k:
                i = i.next  # left
            if n > k:
                j = j.next  # right, notice that j start at head
            curr = curr.next
            n += 1
        i.val, j.val = j.val, i.val
        return head
