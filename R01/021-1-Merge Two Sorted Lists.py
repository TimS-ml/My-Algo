# https://leetcode-cn.com/problems/merge-two-sorted-lists/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        first = head
        while l1 != None and l2 != None:
            if l1.val > l2.val:
                head.next = l2
                l2 = l2.next
            else:
                head.next = l1
                l1 = l1.next
            head = head.next
        if l1 == None:
            head.next = l2
        elif l2 == None:
            head.next = l1
        return first.next


# 有序链表
head1 = ListNode(2)
n1 = ListNode(3)
n2 = ListNode(4)
n3 = ListNode(9)
head1.next = n1
n1.next = n2
n2.next = n3

# 有序链表
head2 = ListNode(3)
m1 = ListNode(5)
m2 = ListNode(7)
m3 = ListNode(8)
head2.next = m1
m1.next = m2
m2.next = m3

res = Solution().mergeTwoLists(head1, head2)
while res:
    print(res.val)
    res = res.next
# print(Solution().mergeTwoLists(head1, head2))
