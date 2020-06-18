# https://leetcode-cn.com/problems/delete-node-in-a-linked-list/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


# 构造链表
head1 = ListNode(2)
n1 = ListNode(3)
n2 = ListNode(4)
n3 = ListNode(9)
head1.next = n1
n1.next = n2
n2.next = n3

# 测试
Solution().deleteNode(n1)

while head1:
    print(head1.val)
    head1 = head1.next
