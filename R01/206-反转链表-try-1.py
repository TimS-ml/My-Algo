# https://leetcode-cn.com/problems/reverse-linked-list/
# ans的结点衔接有问题，一个会超时的半成品


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head) -> ListNode:
        tmp = head
        lenth = 0

        # 计算ListNode的长度
        while tmp:
            tmp = tmp.next
            lenth += 1
        if lenth == 1 or lenth == 0:
            return head
        # print('lenth', lenth)

        ans = ListNode(0)
        tmp = head

        count = lenth - 1  # 如果count = lenth，则带着None
        i = 0
        while count:
            while tmp:
                i += 1
                if i == count:
                    ans.next = tmp  # 直接把当前tmp和后面的node全给了ans
                    # print(ans.next.val)
                    # if i == 3:
                    #     return ans
                    break
                tmp = tmp.next
            tmp = head
            count -= 1
            i = 0
        return ans


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
