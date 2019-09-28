# https://leetcode-cn.com/problems/reverse-linked-list/
# 答案2的正常写法
# 由于节点没有引用其上一个节点，因此必须事先存储其前一个元素
# 在更改引用之前，还需要另一个指针来存储下一个节点
# java里prev = ListNode(null)就行，但是python会包含这个头结点


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    # def __repr__(self):
    #     return str(self.val)


class Solution:
    def reverseList(self, head) -> ListNode:
        if head is None or head.next is None:
            return head

        k = head.val
        prev = ListNode(k)
        curr = head.next

        while curr is not None:
            nextTemp = curr.next  # 存储向前的指针
            curr.next = prev  # 改成向后指针
            prev = curr  # 更新prev
            curr = nextTemp  # 更新curr
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
