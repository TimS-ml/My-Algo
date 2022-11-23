'''
Given the head of a LinkedList and a number 'k', reverse every 'k' sized sub-list starting from the head.
If, in the end, you are left with a sub-list with less than 'k' elements, reverse it too.

# Code Explain:
- Time complexity: O(N)
- Space complexity: O(1)

'''

from __future__ import print_function


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


def reverse_every_k_elements(head, k):
    def reverse(head, b):
        if head == b or head.next == b:
            return head  # the last Node
        last = reverse(head.next, b)
        head.next.next = head
        head.next = None
        return last

    if not head:
        return None
    a, b = head, head

    for _ in range(k):
        if not b:
            return head
        b = b.next

    newHead = reverse(a, b)
    a.next = reverse_every_k_elements(b, k)
    return newHead


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_every_k_elements(head, 3)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()
