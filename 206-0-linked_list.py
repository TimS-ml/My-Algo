'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

# Notation:

'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def xxx(self, head) -> ListNode:
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
