'''
# Code Explain:
- Time complexity: O(N logN)  # slow!!!
- Space complexity: O(N)

each linked-list is sorted in ascending order

bring all nudes into a large list
sort (N logN)
conenct the list
go over the node 3 times: append to list + sort + connect
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# a better Brute Force
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        self.nodes = []
        head = point = ListNode(0)
        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next
        for x in sorted(self.nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next

