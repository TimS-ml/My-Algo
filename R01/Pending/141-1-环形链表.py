# https://leetcode-cn.com/problems/linked-list-cycle/


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# 使用快慢指针，若指针相遇则判断有环
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = slow = head
        while fast and fast.next:
            # delta v = 1
            # 只要slow进了loop，则fast和slow的相对位置会缩小1
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False


# 有序链表
head1 = ListNode(1)
n1 = ListNode(2)
n2 = ListNode(3)
n3 = ListNode(4)
head1.next = n1
n1.next = n2
n2.next = n3  # 快指针会在没有环形的情况下结束
# n3.next = n2  # 快指针会停留在n3：n3->n2->n3
print(Solution().hasCycle(head1))
