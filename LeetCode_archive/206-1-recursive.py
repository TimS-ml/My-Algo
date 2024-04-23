'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(N)
    - The extra space comes from implicit stack space due to recursion, up to n levels deep

In a recursive, we need:
    [1] a simple base case(s), not a terminating senario
        - head.next.next = head  # add pointer: i <- i+1
        - head.next = None  # remove current pointer
    [2] a set of rules: recurrence relation
        - self.reverseList(head.next)
    [3] terminating senario
        - end of linked list or only one node left
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        ans = self.reverseList(head.next)
        head.next.next = head  # add pointer: i <- i+1
        head.next = None  # remove pointer: i -> i+1
        return ans

    # 1 -> 2 -> 3 <- 4 <- 5
    #      |    |
    #     head prev
    # actually you don't change `prev`
    # [1] use: prev = reverse(head.next) to reach the end of the LinkedList
    # [2] use: return prev to go back step by step
    def reverseList_2(self, head: ListNode) -> ListNode:
        def reverse(node):  # return previous node
            # base case
            if not node or not node.next:
                return node

            # state transfer
            # prev is an reversed linked list!!!
            # xxx -> node -> reverse(node.next <- xxx)
            #              |
            #   This is what you want to change
            prev = reverse(node.next)

            # post order
            node.next.next = node  # add pointer: i <- i+1
            node.next = None  # remove pointer: i -> i+1
            return prev

        return reverse(head)


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


line = [1, 2, 3, 4, 5]
head = listToListNode(line)
ans = Solution().reverseList_3(head)
out = listNodeToString(ans)
print(out)
