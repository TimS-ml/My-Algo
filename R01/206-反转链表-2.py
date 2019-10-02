# https://leetcode-cn.com/problems/reverse-linked-list/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)


class Solution:
    def reverseList(self, head) -> ListNode:
        p, rev = head, None
        # 多元赋值的时候，右边的值不会随着赋值而改变
        # print(rev, p)
        while p:
            # 左边的rev被赋值为1，右边的rev还是None
            rev, rev.next, p = p, rev, p.next
            print(rev, p)
        return rev


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