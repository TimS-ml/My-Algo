'''
# Code Explain:
- Time complexity: O(n)
- Space complexity: O(n)
    - The extra space comes from implicit stack space due to recursion, up to n levels deep

In a recursive, we need:
    [1] a simple base case(s), not a terminating senario
        - swap 2 nodes
        - return the head of this case (2nd node)
    [2] a set of rules: recurrence relation
        - func(2nd node.next)
    [3] terminating senario
        - end of linked list or only one node left

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
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        first = head
        second = head.next
        first.next = self.swapPairs(second.next)  # third
        second.next = first
        return second


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
