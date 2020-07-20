'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()
    - The extra space comes from implicit stack space due to recursion, up to n levels deep

What we can do there is to simply have two pointers, one at the beginning of the array and one at the end ('left' and 'right').
We repeatedly swap elements pointed to by these two pointers and we move both the pointers towards the center of the array.

However, we don't have any backward pointers in our linked list and neither do we have any indexes. (Question requires do it in one-pass)
So, we rely on recursion to simulate the backward pointer. We need a function to do the job.

In a recursive, we need:
    [1] a simple base case(s), not a terminating senario
    [2] a set of rules: recurrence relation
    [3] terminating senario

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
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head or not head.next:
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
