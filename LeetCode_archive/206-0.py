'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(1)

Reverse the pointers of Linked List
Since pointer only goes in one way, we need to write a loop until element.next = None
    [1] change the direction of pointers of each node,
    [2] need to create a temp element

Empty Linked List:
    return head
Start of Linked List:
    we initialized prev to None
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # if not head or not head.next:
        #     return head
        prev = None
        while head:
            temp = head
            head = head.next  # move to next, step ahead than temp
            temp.next = prev  # change the pointer
            prev = temp  # update prev
        return prev  # you can return temp as well

    def reverseList_2(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head  # the last Node
        last = self.reverseList_2(head.next)
        head.next.next = head
        head.next = None
        return last


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
ans = Solution().reverseList_2(head)
out = listNodeToString(ans)
print(out)
