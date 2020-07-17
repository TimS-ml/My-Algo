'''
# Code Explain:
- Time complexity: O(n)
- Space complexity: O(1)

In a recursive, we need:
    [1] a simple base case(s)
        not a terminating senario
        head.next.next = head  # add pointer: i <- i+1
        head.next = None  # remove current pointer
    [2] a set of rules: recurrence relation
        self.reverseList(head.next)

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
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        ans = self.reverseList(head.next)
        head.next.next = head  # add pointer: i <- i+1
        head.next = None  # remove current pointer
        return ans


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
