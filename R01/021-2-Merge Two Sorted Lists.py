# https://leetcode-cn.com/problems/merge-two-sorted-lists/
# 换了一种ListNode输入的形式而已，别的没有变化


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


head1_list = [2, 3, 4, 9]
head1 = tmp = ListNode(head1_list[0])  # 设定tmp是为了不改变head1
for i in range(len(head1_list)-1):
    tmp.next = ListNode(head1_list[i+1])
    tmp = tmp.next
# while head1:
#     print(head1.val)
#     head1 = head1.next

head2_list = [3, 5, 7, 8]
head2 = tmp = ListNode(head2_list[0])  # 设定tmp是为了不改变head2
for i in range(len(head2_list)-1):
    tmp.next = ListNode(head2_list[i+1])
    tmp = tmp.next
# while head2:
#     print(head2.val)
#     head2 = head2.next

res = Solution().mergeTwoLists(head1, head2)
while res:
    print(res.val)
    res = res.next

# print(Solution().mergeTwoLists(head1, head2))  # 直接print输出的是内存的地址
