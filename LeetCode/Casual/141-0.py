'''
# Code Explain:
- Time complexity: O(n)
    - Or O(n+k) depends on the cyclic length
- Space complexity: O(1)

# Pros and Cons:
## Pros:
- O(1) Space complexity
- The best case is, no loop, O(n)
    worse case is k = n

## Cons:

# Notation:
The solution 2 is not that elegant
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False

    def hasCycle_2(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        fast = head.next
        slow = head
        while slow != fast:
            if not fast or not fast.next:
                return False
            fast = fast.next.next
            slow = slow.next
        return True


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
