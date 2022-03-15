'''
# Code Explain:
- Time complexity: O(N logN)
- Space complexity: O(N)

each linked-list is sorted in ascending order

sol 1
bring all nudes into a large list
sort (N logN)
conenct the list
go over the node 3 times: append to list + sort + connect


sol 2
O(kN) where k is the number of linked lists.
two pointer, keep a sorted long linked list
go over all nodes even more times
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
        
