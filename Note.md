# Linked List

Pointer of Linked List in python is implemented by value pair:

```py
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
```

For example:
  1 -> 2 -> 3 -> 4

Pointer 2 to 3: 
  - node.val = 2
  - node.next = 3
- update pointer from a to b (globally):
  a.next = b

Position 2:
  - node.val = 2
- move var x from node a to b:
  x = b
- we can build a hash table just like list

So:
  a.next = b
  x = a
Then: x.next is b

LC 328:
```py
def oddEvenList(self, head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    odd = head
    even = head.next
    even_head = even
    while even and even.next:
        odd.next = even.next  # odd pointer
        odd = odd.next  # move odd position
        even.next = odd.next
        even = even.next
    odd.next = even_head
    return head
```
even head is a variable at the beginning position

