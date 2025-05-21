'''
# Code Explain:
- Time complexity: O(N)
    - Or O(n+k) depends on the cyclic length
- Space complexity: O(1)

'''

from typing import List, Optional, Callable


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # same as lc 141
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                break

        # no cycle
        if not fast or not fast.next:
            return None

        slow = head  # or you can put fast to head, same thing
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow


def listToListNode(input):
    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in input:
        ptr.next = ListNode(number)
        ptr = ptr.next
    ptr = dummyRoot.next
    return ptr


def listNodeToString(node):
    if not node:
        return "[]"
    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"

current_solution: Callable[[Optional[ListNode]], Optional[ListNode]] = None

def run_tests(input_file: str):
    global current_solution
    sol = Solution()
    
    # Change this to the function you want to test
    current_solution = sol.detectCycle

    try:
        with open(input_file, 'r') as file:
            test_case = 1
            while True:
                # Read the number of nodes
                n = int(file.readline().strip())
                if n == 0:  # End of file
                    break
                
                # Read the node values
                values = list(map(int, file.readline().strip().split()))
                
                # Read the position of cycle (-1 if no cycle)
                pos = int(file.readline().strip())
                
                # Create linked list
                nodes = [ListNode(val) for val in values]
                for i in range(n-1):
                    nodes[i].next = nodes[i+1]
                
                # Create cycle if pos != -1
                if pos != -1 and pos < n:
                    nodes[-1].next = nodes[pos]
                
                # Expected output is the index of the node where cycle begins
                expected_pos = pos
                
                # Run the solution
                result = current_solution(nodes[0] if n > 0 else None)
                
                # The result is a node object, so we need to find its position in the list
                result_pos = -1
                if result is not None:
                    # Find the index of result node in our nodes list
                    for i, node in enumerate(nodes):
                        if node == result:
                            result_pos = i
                            break
                
                print(f"Test Case {test_case}: {result_pos}, {'Correct' if result_pos == expected_pos else 'Wrong'}")
                
                test_case += 1

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    run_tests("142.txt")
