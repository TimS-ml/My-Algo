# https://leetcode-cn.com/problems/reverse-linked-list/
# This is slower than solution 1
# Multivariate assignment
# the value on the right will not change
# When left rev changed to 1, right rev still unchange
# rev, rev.next, p = p, rev, p.next


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head) -> ListNode:
        p, rev = head, None
        while p:
            # multivariate assignment
            rev, rev.next, p = p, rev, p.next
        return rev


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

ans = Solution().reverseList(head)

out = listNodeToString(ans)
print(out)
