'''
# Code Explain:
- Time complexity: O(NlogN)
- Space complexity: O(1)

'''

from typing import List, Callable


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()  # sort by start is ok
        ans = 0
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            # non-overlapping
            if start >= prevEnd:
                prevEnd = end
            # [1] the best rule to achieve minimum del is not (non-overlapping)
            #     which is min End
            # [2] we don't need to modify the array, only return the count
            else:
                ans += 1
                prevEnd = min(end, prevEnd)
        return ans


current_solution: Callable[[List[List[int]]], int] = None

# run_tests_raw requires the input like this:
# [[1,2],[2,3],[3,4],[1,3]]
# 1
# [[1,2],[1,2],[1,2]]
# 2
# def run_tests_raw(input_file: str):
#     global current_solution
#     sol = Solution()

#     current_solution = sol.eraseOverlapIntervals

#     try:
#         with open(input_file, 'r') as file:
#             test_case = 1
#             while True:
#                 intervals_str = file.readline().strip()
#                 if not intervals_str:
#                     break

#                 intervals = eval(intervals_str)  # Convert string representation to list of lists
#                 expected = int(file.readline().strip())

#                 result = current_solution(intervals)
#                 print(f"Test Case {test_case}: {result}, {'Correct' if result == expected else 'Wrong'}")

#                 test_case += 1

#     except FileNotFoundError:
#         print(f"Error: File '{input_file}' not found.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

def run_tests(input_file: str):
    global current_solution
    sol = Solution()
    
    # Change this to the function you want to test
    current_solution = sol.eraseOverlapIntervals

    try:
        with open(input_file, 'r') as file:
            test_case = 1
            while True:
                # Read the number of intervals
                n = int(file.readline().strip())
                if n == 0:  # End of file
                    break
                
                # Read the intervals
                intervals = []
                for _ in range(n):
                    interval = list(map(int, file.readline().strip().split()))
                    intervals.append(interval)
                
                # Read the expected answer
                expected = int(file.readline().strip())
                
                result = current_solution(intervals)
                print(f"Test Case {test_case}: {result}, {'Correct' if result == expected else 'Wrong'}")
                
                test_case += 1

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_tests("435.txt")
