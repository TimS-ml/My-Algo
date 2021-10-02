'''
# Code Explain:
- Time complexity: O(n)
- Space complexity: O(n)
Key point is, how to mark nodes

# Pros and Cons:
## Pros:
- O(n) time complexity, since we only need to go through each nodes once
## Cons:
- O(n) space complexity

# Notation:
[1]
-1
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        dic = {}
        while head:
            if head in dic:
                return True
            else:
                dic[head] = 1  # mark
            head = head.next
        return False


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
