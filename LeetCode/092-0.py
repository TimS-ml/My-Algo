'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(1)

Reverse the pointers of Linked List
Same like lc 206
    - We need a temp pointer that will help us continue the link reversal process

Essentially, starting from the node at position m and all the way up to n, we reverse the next pointers for all the nodes in between. 

And then connect the pieces together
    - We need to process 2 connections

  m = 2, n = 4
  1 -> 2 -> 3 -> 4 -> 5
  |    |
 con  tail

  1 -> 2 <- 3 <- 4 -> 5
  |    |         |    |
 con  tail     prev  curr

  1 -> 4 -> 3 -> 2 -> 5

# Notation:
- [1] Pay attention to the boundaries
    For example: 
        before reverse: m>1; after: n=0

- [2] Connection
    - If len = n
        - curr = None, so this is not a special case
        - tail.next = curr
    - If m = 1
        - con = None, we need to update head

 None -> 1 <- 2 <- 3 <- 4 -> 5
  |      |              |    |
 con    tail          prev  curr
        head ---------->|

         4 -> 3 -> 2 -> 1 -> 5

    - If m = n
        - this is not a special case
        - reverse on pointer first, then turn back by 
            tail.next = curr

- [3] How many positions do we need to save

- [4] Other special cases
    Empty list

'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween_iter(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return None

        curr, prev = head, None
        while m > 1:
            prev = curr
            curr = curr.next
            m, n = m - 1, n - 1

        tail, con = curr, prev
        # same as lc 206
        while n:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            n -= 1

        if con:
            con.next = prev
        else:
            head = prev

        tail.next = curr

        return head

    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        prev = None
        def reverseN(head: ListNode, n: int):
            nonlocal prev
            if n == 1:
                prev = head.next
                return head
            
            print('before:', '  ' * n, n, prev)
            last = reverseN(head.next, n - 1)
            # prev and last are both fixed
            print('after :', '  ' * n, n, prev.val, last.val)

            head.next.next = head 
            head.next = prev
            return last

        if not head:
            return None

        if m == 1:
            return reverseN(head, n)
        
        head.next = self.reverseBetween(head.next, m - 1, n - 1)
        return head



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
# ans = Solution().reverseBetween(head, 2, 4)
ans = Solution().reverseBetween(head, 1, 4)
out = listNodeToString(ans)
print(out)
