'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

The intuitive way is create an empty linked list and append emement one by one
l1 and l2 may have different length
    - place largest or longest element to the end

sol3 is a in-place solution

# Pros and Cons:
## Pros:

## Cons:

# Notation:

'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = ListNode(0)
        curr = ans
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        curr.next = l1 or l2  # place largest or longest element to the end
        return ans.next

    # If you prefer not create an empty linked list
    def mergeTwoLists_2(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        first = head
        while l1 != None and l2 != None:
            if l1.val > l2.val:
                head.next = l2
                l2 = l2.next
            else:
                head.next = l1
                l1 = l1.next
            head = head.next
        if l1 == None:
            head.next = l2
        elif l2 == None:
            head.next = l1
        return first.next

    # This is a in-place version
    # In-place will be slightly faster
    def mergeTwoLists_3(self, l1: ListNode, l2: ListNode) -> ListNode:
        if None in (l1, l2):
            return l1 or l2
        ans = curr = ListNode(0)
        ans.next = l1  # l1 in-place
        while l1 and l2:
            if l1.val < l2.val:
                l1 = l1.next  # skip these nodes, notice that ans.next = l1
            else:
                temp1 = curr.next
                temp2 = l2.next
                curr.next = l2
                l2.next = temp1
                l2 = temp2
            curr = curr.next
        curr.next = l1 or l2
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


line = [1, 2, 3, 4, 5]
head = listToListNode(line)
ans = Solution().xxx(head)
out = listNodeToString(ans)
print(out)
