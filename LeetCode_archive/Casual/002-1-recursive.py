'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(N)
    Where the N = max(l1, l2)

Put sum result of each digit in l1, rather than create an empty Linked List

In a recursive, we need:
    [1] a simple base case(s), not a terminating senario
    [2] a set of rules: recurrence relation
    [3] terminating senario
        if not (l1 or l2) (both empty)

# Pros and Cons:
## Pros:

## Cons:

# Notation:
both empty doesn't mean "if not a or not b"
    since the latter case only requires one Linked List to be empty
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def add(a, b, carry):
            if not (a or b):
                return ListNode(1) if carry else None

            a = a if a else ListNode(0)
            b = b if b else ListNode(0)

            carry, a.val = divmod(a.val + b.val + carry, 10)
            a.next = add(a.next, b.next, carry)
            return a

        return add(l1, l2, 0)


def listToListNote(input):
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


l1_li = [1, 2, 3, 4, 5]
l2_li = [1, 2, 3, 4, 5]
l1 = listToListNote(l1_li)
l2 = listToListNote(l2_li)
ans = Solution().addTwoNumbers(l1, l2)
out = listNodeToString(ans)
print(out)
