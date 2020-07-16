# https://leetcode-cn.com/problems/merge-two-sorted-lists/
# in-place, and faster (because in-place will jump over some node)


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if None in (l1, l2):
            return l1 or l2
        ans = ListNode(0)
        cur = ans
        ans.next = l1  # l1 in-place
        while l1 and l2:
            if l1.val < l2.val:
                l1 = l1.next  # no need to modify
            else:
                next = cur.next
                cur.next = l2
                temp = l2.next
                l2.next = next
                l2 = temp
            cur = cur.next
        cur.next = l1 or l2
        return ans.next


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


# l1, l2
IN = [([2, 3, 4, 9], [3, 5, 7, 8]), ([], []), ([1, 2, 4], [1, 3, 4])]
useSet = 2
l1 = IN[useSet][0]
l2 = IN[useSet][1]
h1 = listToListNode(l1)
h2 = listToListNode(l2)
ans = Solution().mergeTwoLists(h1, h2)
out = listNodeToString(ans)
print(out)
