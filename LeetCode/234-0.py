'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)


class Solution:
    # post-order traversal of linked list
    def isPalindrome(self, head):
        left = head
        
        def traverse(right):
            nonlocal left
            if not right:
                return True
            ans = traverse(right.next)

            # post-order
            ans = ans and (right.val == left.val)
            left = left.next
            return ans

        return traverse(head)

    # a better optimized space: start from middle
    def isPalindrome_2(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # odd length, move slow to right
        # 1, 2, 3, 2, 1
        # |        |  |
        # head  slow  fast

        # 1, 2, 3, 3, 2, 1, None
        # |        |        |
        # head    slow     fast
        if fast:
            slow = slow.next
        
        def reverse(root):
            pre = None
            cur = root
            while cur:
                tmp = cur.next
                cur.next = pre
                pre = cur
                cur = tmp
            return pre
        
        left = head
        right = reverse(slow)

        while left and right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True 


head1 = ListNode(1)
n1 = ListNode(2)
n2 = ListNode(1)
n3 = ListNode(1)
head1.next = n1
n1.next = n2
n2.next = n3

print(Solution().isPalindrome(head1))
