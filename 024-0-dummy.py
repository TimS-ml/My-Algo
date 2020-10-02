'''
# Code Explain:
- Time complexity: O(n)
- Space complexity: O(1)

Reverse the pointers of Linked List
Since pointer only goes in one way, we need to write a loop until element.next = None
    [1] change the direction of pointers of each node, 
    [2] need to create a temp element

What we need are:
    [1] 3 variables, for each swap invole 3 nodes
        - start at node -1 => so we need a dummy node
        - also, we need to return dummy.next
    [2] variables for pointer (so that we can continue)

# Pros and Cons:
## Pros:
- Dummy node:
    For empty Linked List or len(linked list) = 1:
        return dummy.next
    For len(linked list) = 2:
        we can processed swap
        if we set prev = head, then we need to take care of the particular case where len = 2
## Cons:
- If we use recursive, the code will be cleaner (no dummpy node)

# Notation:

'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy

        while head and head.next:
            first = head
            second = head.next

            prev.next = second
            first.next = second.next
            second.next = first

            prev = first
            head = first.next
        return dummy.next


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
ans = Solution().xxx(head)
out = listNodeToString(ans)
print(out)
