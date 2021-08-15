'''
stack of l1 and l2
- get the length of l1 and l2
    - align l1 and l2
- carry + reminder => divmod
- 2 pointers for each linked list: curr and prev

- calculate final result
- reverse linked list (or create a linked list in reverse order directly)
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1.val == 0:
            return l2
        if l2.val == 0:
            return l1
        stack1, stack2 = [], []
        head1, head2 = l1, l2
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        length1, length2 = len(stack1), len(stack2)
        ans = []

        carry = 0
        # after loop, at lease 1 stack is empty
        # carry may != 0
        while stack1 and stack2:
            dig = stack1.pop() + stack2.pop() + carry
            val = dig % 10
            ans.append(val)
            carry = dig // 10  # update carry

        remain = stack1 if stack1 else stack2

        while remain:
            dig = remain.pop() + carry
            val = dig % 10
            ans.append(val)
            carry = dig // 10

        if carry != 0:
            ans.append(carry)

        # [7, 0, 8, 7]
        # print(ans)
        # requires len(ans) >= 1

        temp = ListNode(ans[0])
        temp.next = None
        if len(ans) == 1:
            return temp
        for i in range(1, len(ans)):
            curr = ListNode(ans[i])
            curr.next = temp
            # update temp Node
            temp = curr
        return curr
