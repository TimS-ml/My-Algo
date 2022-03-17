'''
# Code Explain:
Sol 1
- Time complexity: O(N logK)
K is the number of linked lists.
- Space complexity: O(1)

Sol 2
- Time complexity: O(N logK)
K is the number of linked lists.
- Space complexity: O(N)

Sol 1
Merge with Divide And Conquer
- Pair up k lists and merge each pair
- After the first pairing, k lists are merged into k/2 lists with average 2N/k length, 
    then k/4, k/8 and so on
- Repeat this procedure until we get the final sorted linked list

Sol 2
Merge Sort Template
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        bottom up merge sort, terrible written in my opinion
        official solution, not our template
        """
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else None

    def merge2Lists(self, l1, l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l1
                l1 = point.next.next
            point = point.next
        if not l1:
            point.next=l2
        else:
            point.next=l1
        return head.next


class Solution2(object):
    def mergeKLists(self, lists):
        """
        trying to use merge sort template
        https://leetcode.com/problems/merge-k-sorted-lists/discuss/10640/Simple-Java-Merge-Sort
        """

        def sort(lists, low, high):
            if low >= high:
                return lists[low]
            mid = int(low + (high - low) / 2)
            l1 = sort(lists, low, mid)
            l2 = sort(lists, mid + 1, high)
            return merge(l1, l2)
    
        def merge(l1, l2):
            if not l1:
                return l2
            if not l2:
                return l1
            if l1.val < l2.val:
                l1.next = merge(l1.next, l2)
                return l1
            else:
                l2.next = merge(l1, l2.next)
                return l2
    
        if len(lists) == 0:
            return None
        return sort(lists, 0, len(lists) - 1)
