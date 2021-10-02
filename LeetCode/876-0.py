'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

# Pros and Cons and Notation:
用两个指针 slow 与 fast 一起遍历链表
那么当 fast 到达链表的末尾时, slow 必然位于中间
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        # A = [head]
        # while A[-1].next:
        #     A.append(A[-1].next)
        # return A[len(A) // 2]

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
