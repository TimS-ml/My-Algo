# https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)


class Solution:
    def removeNthFromEnd(self, head, n) -> ListNode:
        dummy = ListNode(-1)  # 哑结点，在头部，以应对极端情况
        dummy.next = head
        fast = slow = dummy

        while n and fast:  # 让fast先向前跑n步
            fast = fast.next
            n -= 1
            # print(n)

        while fast.next and slow.next:  # 当fast跑到末尾的时候slow整好是倒数第n-1个节点
            fast = fast.next
            slow = slow.next
            # print(fast, slow)

        slow.next = slow.next.next
        return dummy.next


head1_list = [1, 2, 3, 4, 5]
head1 = tmp = ListNode(head1_list[0])  # 设定tmp是为了不改变head1
for i in range(len(head1_list)-1):
    tmp.next = ListNode(head1_list[i+1])
    tmp = tmp.next
# while head1:
#     print(head1.val)
#     head1 = head1.next

# Solution().removeNthFromEnd(head1, 2)

res = Solution().removeNthFromEnd(head1, 2)
while res:
    print(res.val)
    res = res.next
