'''
using stack
keep in mind of the 'reverse'

'''

from typing import Optional, List, Callable


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1, s2 = [], []

        while l1:
            s1.append(l1.val)
            l1 = l1.next

        while l2:
            s2.append(l2.val)
            l2 = l2.next
        
        res = None
        c = 0  # carry
        while s1 or s2 or c:  # NOTE: check if c is zero!!!
            d1, d2 = s1.pop() if s1 else 0, s2.pop() if s2 else 0
            c, dig = divmod(d1 + d2 + c, 10)
            n = ListNode(dig)
            n.next = res
            res = n

        return res

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node
        return prev

    def addTwoNumbers_2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)

        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)
            carry, out = divmod(val1+val2+carry, 10)

            current.next = ListNode(out)
            current = current.next

            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)

        return self.reverseList(dummy.next)


def list_to_linkedlist(arr: List[int]) -> Optional[ListNode]:
    dummy = ListNode(0)
    current = dummy
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def linkedlist_to_list(head: Optional[ListNode]) -> List[int]:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

current_solution: Callable[[Optional[ListNode], Optional[ListNode]], Optional[ListNode]] = None

def run_tests(input_file: str):
    global current_solution
    sol = Solution()
    
    # Change this to the function you want to test
    current_solution = sol.addTwoNumbers

    try:
        with open(input_file, 'r') as file:
            test_case = 1
            while True:
                l1 = list(map(int, file.readline().strip().split()))
                if not l1:  # End of file
                    break
                l2 = list(map(int, file.readline().strip().split()))
                expected = list(map(int, file.readline().strip().split()))
                
                l1_node = list_to_linkedlist(l1)
                l2_node = list_to_linkedlist(l2)
                
                result = current_solution(l1_node, l2_node)
                result_list = linkedlist_to_list(result)
                
                print(f"Test Case {test_case}:")
                print(f"Input: l1 = {l1}, l2 = {l2}")
                print(f"Output: {result_list}")
                print(f"Expected: {expected}")
                print(f"Result: {'Correct' if result_list == expected else 'Wrong'}")
                print()
                
                test_case += 1

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_tests("445.txt")
