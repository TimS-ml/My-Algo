'''
# Code Explain:
- Time complexity: O(N logK)
K is the number of linked lists.
- Space complexity: O(1)

https://leetcode.com/problems/merge-k-sorted-lists/discuss/10511/10-line-python-solution-with-priority-queue
https://leetcode.com/problems/merge-k-sorted-lists/discuss/1745539/Python3-PRIORITY-QUEUE-()-Explained

key idea:
- same to:
    - given a list of k linked lists, create k pointer
'''

from queue import PriorityQueue
import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        curr = head = ListNode(0)
        queue = PriorityQueue()
        count = 0

        for node in lists:
            # only the 'curr' in queue
            if node:
                # priority, node
                # In the event that two or more of the lists have the same val,
                # this code will error out
                # since the queue module will compare the second element in the priority queue
                # which is a ListNode object (and this is not a comparable type)
                queue.put((node.val, count, node))
                count += 1

        while not queue.empty():
            # val, _, node = queue.get()
            # curr.next = ListNode(val)
            # curr = curr.next
            # node = node.next

            # # replace node with node.next
            # # without count, will return error
            # if node:
            #     queue.put((node.val, count, node))
            #     count += 1

            _, _, curr.next = queue.get()
            curr = curr.next

            # replace node with node.next
            # without count, will return error
            if curr.next is not None:
                queue.put((curr.next.val, count, curr.next))
                count += 1

        return head.next

    # a heap implementation
    def mergeKLists_2(self, lists: List[ListNode]) -> ListNode:
        curr = head = ListNode(0)
        heap = []

        count = 0
        for node in lists:
            if node is not None:
                count += 1
                # if same node.val, compare count
                heapq.heappush(heap, (node.val, count, node))

        while len(heap) > 0:
            # assign val to curr.next
            _, _, curr.next = heapq.heappop(heap)
            
            # move forward
            curr = curr.next
            if curr.next is not None:
                count += 1
                heapq.heappush(heap, (curr.next.val, count, curr.next))
        return head.next  # remember this!!!
