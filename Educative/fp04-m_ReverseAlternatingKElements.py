'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

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


def reverse_alternate_k_elements(head, k):

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

    # New: skip 'k' nodes
    a.next = b
    for _ in range(k):
        if not a:
            return newHead
        a = a.next
    
    if a:
        a.next = reverse_alternate_k_elements(a.next, k)
    return newHead


def reverse_alternate_k_elements_ref(head, k):
    temp = head

    for _ in range(k):
        if temp == None:
            return head
        temp = temp.next

    ## reverse firt k if length > k
    prev = None
    curr = head
    for _ in range(k):
        future = curr.next
        curr.next = prev
        prev = curr
        curr = future

    if head != None:
        head.next = curr

    count = 0
    while count < k - 1 and curr:
        curr = curr.next
        count += 1

    if curr:
        curr.next = reverse_alternate_k_elements(curr.next, k)
    return prev


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
    result = reverse_alternate_k_elements(head, 2)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()
