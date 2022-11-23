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
    # although you only need to compare the first half
    # this solution compares full list
    def isPalindrome(self, head):
        left = head

        def traverse(right):
            if not right:
                return True

            ans = traverse(right.next)

            # post-order
            nonlocal left
            # the very first comparison:
            #   left at [0] and right at [-1]
            # if list[x] != list[-(x+1)], ans = False
            # the rest comparison (x+1 to mid) all False
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

        # if even length (1~8)
        # 4 steps, slow at 5 (second middle), fast at None

        # if odd length (1~7)
        # 3 steps, slow at 4 (middle), fast at 7 (not None)

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


    # a very simple solution
    def isPalindrome_3(self, head):
        vals = []
        current_node = head
        while current_node is not None:
            vals.append(current_node.val)
            current_node = current_node.next
        return vals == vals[::-1]


head1 = ListNode(1)
n1 = ListNode(2)
n2 = ListNode(1)
n3 = ListNode(1)
head1.next = n1
n1.next = n2
n2.next = n3

print(Solution().isPalindrome(head1))
