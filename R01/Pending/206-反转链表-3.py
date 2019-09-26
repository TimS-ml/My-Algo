# https://leetcode-cn.com/problems/reverse-linked-list/
# 答案1的简化写法


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    # def __repr__(self):
    #     return str(self.val)


class Solution:
    def reverseList(self, head) -> ListNode:
        prev = None
        curr = head
        while curr:
            nextTemp = curr.next
            curr.next = prev
            prev = curr
            curr = nextTemp
        return prev


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
