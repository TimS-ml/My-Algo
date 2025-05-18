'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()
'''

from typing import List, Callable


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            if target - numbers[l] - numbers[r] > 0:
                l += 1
            elif target - numbers[l] - numbers[r] < 0:
                r -= 1
            else:
                return [l + 1, r + 1]


current_solution: Callable[[List[int], int], List[int]] = None

def run_tests(input_file: str):
    global current_solution
    sol = Solution()
    
    # Change this to the function you want to test
    current_solution = sol.twoSum

    try:
        with open(input_file, 'r') as file:
            test_case = 1
            while True:
                # Read the array size
                n = int(file.readline().strip())
                if n == 0:  # End of file
                    break
                
                # Read the numbers array
                numbers = list(map(int, file.readline().strip().split()))
                
                # Read the target
                target = int(file.readline().strip())
                
                # Read the expected answer
                expected = list(map(int, file.readline().strip().split()))
                
                result = current_solution(numbers, target)
                print(f"Test Case {test_case}: {result}, {'Correct' if result == expected else 'Wrong'}")
                
                test_case += 1

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_tests("167.txt")
