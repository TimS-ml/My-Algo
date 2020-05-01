# https://leetcode-cn.com/problems/reverse-linked-list/
# in java, we can simply write prev = ListNode(null)
# check animation
# https://leetcode-cn.com/problems/reverse-linked-list/solution/fan-zhuan-lian-biao-shuang-zhi-zhen-di-gui-yao-mo-/


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head) -> ListNode:
        if not head or not head.next:
            return head
        ans = self.reverseList(head.next)
        head.next.next = head  # i <- i+1
        head.next = None
        return ans


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

