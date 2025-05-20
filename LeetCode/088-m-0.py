'''
# Code Explain:
- Time complexity: O(N + M)
- Space complexity: O(M)

case1: 
num1 = [1,2,3,0,0,0], num2 = [4,5,6]

case2: 
num1 = [4,5,6,0,0,0], num2 = [1,2,3]
'''

from typing import List, Callable


class Solution:
    # pointers at start, need copy
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pos = m + n - 1
        m -= 1
        n -= 1
        while m >= 0 and n >= 0:
            if nums1[m] > nums2[n]:
                nums1[pos] = nums1[m]
                m -= 1
            else:
                nums1[pos] = nums2[n]
                n -= 1
            pos -= 1

        while n >= 0:
            nums1[pos] = nums2[n]
            n -= 1
            pos -= 1


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
