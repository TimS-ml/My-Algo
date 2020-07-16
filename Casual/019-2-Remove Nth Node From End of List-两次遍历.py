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
        tmp = dummy
        lenth = 0

        # 计算ListNode的长度
        while tmp:
            tmp = tmp.next
            lenth += 1
        # print('lenth', lenth)

        # 修改ListNode，边界问题需要注意
        # 如果count = lenth - n，则一开始进while就会向前推一步，整好是要删除的节点的位置
        tmp = dummy
        count = lenth - n - 1
        print('count', count)
        while count:
            tmp = tmp.next
            count -= 1
            print(tmp, count)  # 最后是3 0

        tmp.next = tmp.next.next
        return dummy.next


head1_list = [1, 2, 3, 4, 5]
head1 = tmp = ListNode(head1_list[0])  # 设定tmp是为了不改变head1
for i in range(len(head1_list) - 1):
    tmp.next = ListNode(head1_list[i + 1])
    tmp = tmp.next
# while head1:
#     print(head1.val)
#     head1 = head1.next

# Solution().removeNthFromEnd(head1, 2)

res = Solution().removeNthFromEnd(head1, 2)
while res:
    print(res.val)
    res = res.next
