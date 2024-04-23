'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(1)

The question is:
How to find n-th node from the end?
The intuitive approach is using 2 loops, first one get the length of Linked List

If we wants one pass, we need to keep the i-n position

We need dummy Nodes, for example
[1], 1 will return []
Or, we can add a if-else as shown in sol 3
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # get length then move
    # def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    #     dummy = ListNode(0)
    #     dummy.next = head
    #     lenth = 0
    #     temp = head  # start at head position

    #     while temp:
    #         temp = temp.next
    #         lenth += 1

    #     temp = dummy
    #     lenth -= n
    #     while lenth > 0:
    #         temp = temp.next
    #         lenth -= 1

    #     temp.next = temp.next.next
    #     return dummy.next

    # two pointers
    def removeNthFromEnd(self, head, n) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        fast = slow = dummy

        for i in range(n):  # make 'fast' n steps ahead
            fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next

    # two pointers, no dummy version
    def removeNthFromEnd_2(self, head, n) -> ListNode:
        fast = slow = head

        for i in range(n):  # make 'fast' n steps ahead
            fast = fast.next

        if not fast:
            return head.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next
