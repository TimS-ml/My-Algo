'''
# Code Explain:
sol 1
- Time complexity: O(N + M)
- Space complexity: O(1)

sol 2
- Time complexity: O(N + M)
- Space complexity: O(M)
'''

from typing import List, Callable


class Solution:
    # pointers at end
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Set p1 and p2 to point to the end of their respective arrays.
        p1 = m - 1
        p2 = n - 1

        # And move p backwards through the array, each time writing
        # the smallest value pointed at by p1 or p2.
        for p in range(n + m - 1, -1, -1):
            if p2 < 0:
                break
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1

    # pointers at start, need copy
    def merge_2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Make a copy of the first m elements of nums1.
        nums1_copy = nums1[:m]

        # Read pointers for nums1Copy and nums2 respectively.
        p1 = 0
        p2 = 0

        # Compare elements from nums1Copy and nums2 and write the smallest to nums1.
        for p in range(n + m):
            # We also need to ensure that p1 and p2 aren't over the boundaries
            # of their respective arrays.
            if p2 >= n or (p1 < m and nums1_copy[p1] <= nums2[p2]):
                nums1[p] = nums1_copy[p1]
                p1 += 1
            else:
                nums1[p] = nums2[p2]
                p2 += 1


# Function to parse a line of space-separated integers
def parse_input_array(input_str: str) -> List[int]:
    if not input_str.strip():
        return []
    return list(map(int, input_str.strip().split()))

current_solution: Callable[[List[int], int, List[int], int], None] = None

def run_tests(input_file: str):
    global current_solution
    sol = Solution()
    
    # Change this to the function you want to test
    current_solution = sol.merge

    try:
        with open(input_file, 'r') as file:
            test_case = 1
            while True:
                # Read m and n
                line = file.readline().strip()
                if not line or line == "0":  # End of file
                    break
                
                m, n = map(int, line.split())
                
                # Read nums1 and nums2
                nums1 = parse_input_array(file.readline().strip())
                nums2 = parse_input_array(file.readline().strip())
                
                # Read the expected answer
                expected_str = file.readline().strip()
                expected = parse_input_array(expected_str)
                
                # Create a copy of nums1 for testing
                nums1_copy = nums1.copy()
                
                # Apply the solution
                current_solution(nums1_copy, m, nums2, n)
                
                # Check if the result matches expected
                result_correct = nums1_copy == expected
                print(f"Test Case {test_case}: {'Correct' if result_correct else 'Wrong'}")
                if not result_correct:
                    print(f"  Expected: {expected}")
                    print(f"  Got: {nums1_copy}")
                
                test_case += 1

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_tests("088.txt")
