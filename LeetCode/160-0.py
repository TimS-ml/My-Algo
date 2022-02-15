'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()


- intersectVal is 0 if listA and listB do not intersect
- intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect
- if skipA and skipB is the last node, then value compare is enough
- otherwise is linked list compare
    - value in common
    - if in common until end of A and B list

sol 1:
convert listA and listB to list
may exceed time limit

sol2:
2 pointers
After pointer A move to the end, move it to B
When the pointer of the longer linked list points to the head of the shorter linked list, the length difference is eliminated
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode,
                            headB: ListNode) -> ListNode:
        visited = []
        A, B = headA, headB
        while A != None:
            visited.append(A)
            A = A.next
        while B != None:
            # ListNode has .val and .next so its possible to recognize the case:
            #   [4,1,8,4,5]
            # [5,6,1,8,4,5]
            if B in visited:
                return B
            B = B.next
        return None

    def getIntersectionNode_2(self, headA: ListNode,
                              headB: ListNode) -> ListNode:
        A, B = headA, headB
        while A != B:
            A = A.next if A else headB
            B = B.next if B else headA
        return A


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


# line = [1, 2, 3, 4, 5]
# head = listToListNode(line)
# ans = Solution().xxx(head)
# out = listNodeToString(ans)
# print(out)
