'''
# Code Explain:
- Time complexity: O(n)
- Space complexity: O(1)

# Pros and Cons and Notation:
Do not try to jump n nodes once, it will bring you a lot of troubles
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        curr, nxt = head, head.next
        while curr.next:
            if curr.val == nxt.val:
                curr.next = nxt.next
                nxt = nxt.next
            else:
                curr = curr.next
                nxt = nxt.next
        return head

    def deleteDuplicates_2(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        curr = head
        while curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
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


line = [1, 1, 2, 3, 3]
head = listToListNode(line)
ans = Solution().deleteDuplicates(head)
out = listNodeToString(ans)
print(out)
