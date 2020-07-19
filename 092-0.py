'''
# Code Explain:
- Time complexity: O(n)
- Space complexity: O(1)

Reverse the pointers of Linked List
Same like lc 206
Reverse part of the list and then connect the pieces together
    - We need to process 2 connections

  m = 2, n = 4
  1 -> 2 -> 3 -> 4 -> 5
  |    |
 con  tail

  1 -> 2 <- 3 <- 4 -> 5
  |    |         |    |
 con  tail     prev  curr

  1 -> 4 -> 3 -> 2 -> 5

# Pros and Cons:
## Pros:

## Cons:

# Notation:

'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return None

        curr, prev = head, None

        while m > 1:
            prev = curr
            curr = curr.next
            m, n = m - 1, n - 1

        tail, con = curr, prev
        while n:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            n -= 1

        if con:
            con.next = prev
        else:
            head = prev

        tail.next = curr

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
