# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# class Do_ListNode(object):
#     def __init__(self):
#         self.root = ListNode()
#         self.myQueue = []

#     def add(self, val):
#         """为ListNode添加节点"""
#         node = TreeNode(val)
# 		head1 = tmp = ListNode(head1_list[0])  # 设定tmp是为了不改变head1
# 		for i in range(len(head1_list)-1):
# 		    tmp.next = ListNode(head1_list[i+1])
# 		    tmp = tmp.next


head1_list = [1, 2, 3, 4, 5]
head1 = tmp = ListNode(head1_list[0])  # 设定tmp是为了不改变head1
for i in range(len(head1_list)-1):
    tmp.next = ListNode(head1_list[i+1])
    tmp = tmp.next
# while head1:
#     print(head1.val)
#     head1 = head1.next

res = Solution().removeNthFromEnd(head1, 2)
while res:
    print(res.val)
    res = res.next