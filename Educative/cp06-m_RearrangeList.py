'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

the nodes from the second half of the LinkedList are inserted alternately
    to the nodes from the first half in reverse order
So if the LinkedList has nodes 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null,
your method should return 1 -> 6 -> 2 -> 5 -> 3 -> 4 -> null.
'''


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(str(temp.value) + " ", end='')
            temp = temp.next
        print()


def reorder(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # if even length (1~8)
    # 4 steps, slow at 5 (second middle), fast at None

    # if odd length (1~7)
    # 3 steps, slow at 4 (middle), fast at 7 (not None)

    if fast:
        slow = slow.next

    def reverse(root):
        pre = None
        cur = root
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre

    left = head
    right = reverse(slow)

    while left and right:
        temp = left.next
        left.next = right
        left = temp

        temp = right.next
        right.next = left
        right = temp

    # set the next of the last node to 'None'
    if left is not None:
        left.next = None


def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)
    head.next.next.next.next.next = Node(12)
    reorder(head)
    head.print_list()


main()
