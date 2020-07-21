'''
# Code Explain:
- Time complexity: O(n)
- Space complexity: O(n)
    - The extra space comes from implicit stack space due to recursion, up to n levels deep

This is inspired by lc 92

In a recursive, we need:
    [1] a simple base case(s), not a terminating senario
        - head.next.next = head  # add pointer: i <- i+1
        - head.next = None  # remove current pointer
    [2] a set of rules: recurrence relation
        - self.reverseList(head.next)
    [3] terminating senario
        - end of linked list or only one node left

# Pros and Cons:
## Pros:

## Cons:
- We need to change the value of Linked List

# Notation:

'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        temp = head
        n = 0
        while temp:
            temp = temp.next
            n += 1

        l, r = head, head
        stop = False
        def recurse_and_reverse(r, n):
            nonlocal l, stop
            
            # Part 1
            # base case
            if n == 1:
                return
            
            # move to the proper node
            r = r.next

            recurse_and_reverse(r, n-1)

            # Part 2
            if l == r or l == r.next:
                stop = True

            if not stop:
                l.val, r.val = r.val, l.val
                # r moves one step back via backtracking
                l = l.next

        recurse_and_reverse(r, n)
        return head


def listToListNode(input):
    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in input:
        ptr.next = ListNode(number)
        ptr = ptr.next
    ptr = dummyRoot.next
    return ptr


def listNodeToString(node):
    if not node:
        return "[]"
    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


line = [1, 2, 3, 4, 5]
head = listToListNode(line)
ans = Solution().xxx(head)
out = listNodeToString(ans)
print(out)
