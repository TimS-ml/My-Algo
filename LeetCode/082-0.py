'''
# Code Explain:
- Time complexity: O(n)
- Space complexity: O(1)

# Pros and Cons and Notation:
- if you need to modify head, add a dummy and set dummy.next = head, it will save you a lot of time
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head

        dummy = ListNode(0)
        dummy.next = head

        curr = dummy
        while curr.next and curr.next.next:
            if curr.next.val == curr.next.next.val:
                x = curr.next.val
                while curr.next and curr.next.val == x:
                    curr.next = curr.next.next
            else:
                curr = curr.next

        return dummy.next


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


# line = [1, 2, 3, 3, 4, 4, 5]
line = [1, 1, 1, 2, 3, 4, 5]
head = listToListNode(line)
ans = Solution().deleteDuplicates(head)
out = listNodeToString(ans)
print(out)
