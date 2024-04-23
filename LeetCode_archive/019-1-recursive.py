'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(N)
We can recursively find out n-th node from the end
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        def helper(head):
            if not head:
                return 0, head
            i, head.next = helper(head.next)
            return i + 1, (head, head.next)[i + 1 == n]

        return helper(head)[1]

    # a easier version
    def removeNthFromEnd_2(self, head, n):
        def helper(n, head):
            # at end
            if not head:
                return 0, head

            # start with 0, l[-1], then 1, l[-2]...
            i, node = helper(n, head.next)
            # print(i, head.val)

            i += 1
            head.next = node
            if i == n:
                head = head.next
            return i, head

        return helper(n, head)[1]
