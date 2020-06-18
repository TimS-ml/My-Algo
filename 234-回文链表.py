# https://leetcode-cn.com/problems/palindrome-linked-list/
# reverse之后会破坏原来的head
# 所以如果要全反转全对比需要修改reverse函数


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)


class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        def reverseList(root):
            pre = None
            cur = root
            while cur:
                tmp = cur.next
                cur.next = pre
                pre = cur
                cur = tmp
            return pre

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # print(slow, slow.next)

        # 相当于调转后半部分
        newHead = reverseList(slow)
        p1 = head
        p2 = newHead
        while p1 and p2:
            print(p1, p2)
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        return True


head1 = ListNode(1)
n1 = ListNode(2)
n2 = ListNode(1)
n3 = ListNode(1)
head1.next = n1
n1.next = n2
n2.next = n3

print(Solution().isPalindrome(head1))
