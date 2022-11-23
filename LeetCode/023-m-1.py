'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import heapq
from heapq import heappush, heappop

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = []
        ans = ListNode()

        count = 0
        for l in lists:
            heappush(h, count, l)
            count += 1

        while h:  # TODO
            node = heappop(h)
            ans.next = node
            if node.next:
                heappush(h, count, node.next)
            count += 1

        return ans.next
