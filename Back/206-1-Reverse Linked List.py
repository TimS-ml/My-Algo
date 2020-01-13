# https://leetcode-cn.com/problems/reverse-linked-list/
# in java, we can simply write prev = ListNode(null)


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head) -> ListNode:
        prev = None
        curr = head
        while curr:
            nextTemp = curr.next  # save pointer ->
            curr.next = prev  # change to <-
            prev = curr  # prev move to next
            curr = nextTemp  # curr move to next
        return prev


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
