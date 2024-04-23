'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge_sort(node):
            if not node or not node.next:
                return node
            mid = get_mid(node)
            left_arr = merge_sort(node)
            right_arr = merge_sort(mid)
            return merge(left_arr, right_arr)

        def merge(arr1, arr2):
            tail = dummy = ListNode()

            while arr1 and arr2:
                if arr1.val < arr2.val:
                    tail.next = arr1
                    arr1 = arr1.next
                else:
                    tail.next = arr2
                    arr2 = arr2.next
                tail = tail.next

            tail.next = arr1 or arr2
            return dummy.next

        def get_mid(node):
            fast, slow = node.next, node
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            mid = slow.next
            slow.next = None
            return mid

        return merge_sort(head)
