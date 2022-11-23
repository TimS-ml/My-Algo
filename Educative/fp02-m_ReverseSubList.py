'''
Given the head of a LinkedList and two positions 'p' and 'q', reverse the LinkedList from position 'p' to 'q'.

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


def reverse_sub_list(head, m, n):
    prev = None
    def reverseN(head, n):
        nonlocal prev
        if n == 1:
            prev = head.next
            return head

        last = reverseN(head.next, n - 1)
        head.next.next = head
        head.next = prev
        return last

    if m == 1:
        return reverseN(head, n)

    head.next = reverse_sub_list(head.next, m - 1, n - 1)
    return head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_sub_list(head, 2, 4)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()
