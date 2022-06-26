'''
Given the head of a Singly LinkedList that contains a cycle, write a function to find the starting node of the cycle.

# Code Explain:
- Time complexity: O(N)
- Space complexity: O(1)


lc 141 and lc 142
'''

from __future__ import print_function


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end='')
            temp = temp.next
        print()


def find_cycle_start(head):
    fast = slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            break

    # no cycle
    if not fast or not fast.next:
        return None

    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))


main()
