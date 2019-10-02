# https://leetcode-cn.com/problems/reverse-linked-list/
# 没仔细看，感觉是原地算法


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, root) -> ListNode:
        if not root or not root.next:
            return root
        ret = self.reverseList(root.next)
        root.next.next = root
        root.next = None
        return ret

    def _reverseList(self, head):
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre

    # iteratively as queue head inserting
    def __reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dHead = dummy = ListNode(-1)
        p = head
        while p:
            tmp = dummy.next
            dummy.next = p
            p = p.next
            dummy.next.next = tmp
        return dHead.next

    # easily leads to a circle.
    # remove current node's next after recursive call.
    def ___reverseList(self, head):
        self.newHead = None

        def rec(head):
            if not head:
                return head
            p = rec(head.next)
            head.next = None
            if p:
                p.next = head
            else:
                self.newHead = head
            return head

        rec(head)
        return self.newHead


head1 = ListNode(1)
n1 = ListNode(2)
n2 = ListNode(3)
n3 = ListNode(4)
n4 = ListNode(5)
n5 = ListNode(None)
head1.next = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
# while head1:
#     print(head1.val)
#     head1 = head1.next

res = Solution().reverseList(head1)
while res:
    print(res.val)
    res = res.next
