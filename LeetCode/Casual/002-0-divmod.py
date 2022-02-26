'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(N)
    Where the N = max(l1, l2)

Same as LC 066 "Plus One"
Define a variable called carry
Take care of the situations like 999 + 1

# Pros and Cons:
## Pros:

## Cons:

# Notation:

'''

# import pysnooper


# @pysnooper.snoop()
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr = ans = ListNode(0)
        carry = 0
        while l1 and l2:
            curr.next = ListNode((l1.val + l2.val + carry) % 10)  # reminder
            carry = (l1.val + l2.val + carry) // 10  # divide exactly
            # carry, val = divmod(l1.val + l2.val + carry, 10)
            # curr.next = ListNode(val)
            l1 = l1.next
            l2 = l2.next
            curr = curr.next

        longer = l1 or l2
        while longer:
            curr.next = ListNode((longer.val + carry) % 10)  # reminder
            carry = (longer.val + carry) // 10  # divide exactly
            longer = longer.next
            curr = curr.next

        if carry:
            curr.next = ListNode(1)

        return ans.next

    # a shorter version
    def addTwoNumbers_2(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr = ans = ListNode(0)
        carry = 0
        while l1 or l2:
            val = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry, reminder = divmod(val, 10)
            curr.next = ListNode(reminder)
            l1 = l1 and l1.next  # 1 and None => None
            l2 = l2 and l2.next
            curr = curr.next
        # We can remove this "if" by changing the "while loop" to the following:
        # while l1 or l2 or carry
        if carry != 0:
            curr.next = ListNode(1)
        return ans.next


def listToListNode(input):
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


# l1_li = [1, 2, 3, 4, 5]
# l2_li = [1, 2, 3, 4, 5]
l1_li = [2, 4, 3]
l2_li = [5, 6, 4, 1]
l1 = listToListNode(l1_li)
l2 = listToListNode(l2_li)
ans = Solution().addTwoNumbers_2(l1, l2)
out = listNodeToString(ans)
print(out)
