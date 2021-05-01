''' 
# Thought process

- Number is stored in reverse order
  - the answer should also in reverse order 
- Do not contain any leading zero (except number 0)
- Difference length of l1 and l2

Example:
[2, 4, 3]
[5, 6, 4, 1]
    |
  6 + 4 >= 10
carry = (l1.val + l2.val) // 10

ans = 7 0 8 1

[1] We can do this in-place, digit by digit
[2] Loop through the longest one
[3] Need a var to save 'carry'
  - what if carry >= 1 after loop?

# Test case
[2, 4, 3]
[5, 6, 4, 1]

[2, 4, 3]
[0]

[9, 9, 9, 9]
[1]
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr = ans = ListNode(0)
        carry = 0
        while l1 or l2:
            val = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry, reminder = divmod(val, 10)
            curr.next = ListNode(reminder)
            l1 = l1 and l1.next  # 1 and None => None
            l2 = l2 and l2.next
            curr = curr.next
        if carry != 0:
            curr.val = carry
        return ans.next


def listToListNote(input):
    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in input:
        ptr.next = ListNode(number)
        ptr = ptr.next
    ptr = dummyRoot.next
    return ptr


def listNodeToString(node):
    if not node:
        return "[]"
    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


l1_li = [2, 4, 3]
l2_li = [5, 6, 4, 1]
l1 = listToListNote(l1_li)
l2 = listToListNote(l2_li)
ans = Solution().addTwoNumbers(l1, l2)
out = listNodeToString(ans)
print(out)
