'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def is_palindromic_linked_list(head):
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
        if left.val != right.val:
            return False
        left = left.next
        right = right.next

    return True


def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)

    print("Is palindrome: " + str(is_palindromic_linked_list(head)))

    head.next.next.next.next.next = Node(2)
    print("Is palindrome: " + str(is_palindromic_linked_list(head)))


main()
