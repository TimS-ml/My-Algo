'''
# Code Explain:
- Time complexity: O(n)
- Space complexity: O(n)
We can recursively find out n-th node from the end

# Pros and Cons:
## Pros:

## Cons:

# Notation:

'''

# import pysnooper


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# @pysnooper.snoop()
class Solution:
    def removeNthFromEnd(self, head, n):
        def remove(head):
            if not head:
                return 0, head
            i, head.next = remove(head.next)
            return i+1, (head, head.next)[i+1 == n]
        return remove(head)[1]


    # a easier version
    def removeNthFromEnd_2(self, head, n):
        def remove(n, head):            
            if not head:
                return 0, head
            i, node = remove(n, head.next)
            print(i, head.val)
            i += 1
            head.next = node
            if i == n:
                head = head.next
            return i, head
        return remove(n, head)[1]


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
ans = Solution().removeNthFromEnd_2(head, 2)
out = listNodeToString(ans)
print(out)

