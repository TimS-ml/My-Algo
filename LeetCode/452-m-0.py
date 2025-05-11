'''
# Code Explain:
- Time complexity : O(NlogN) 
- Space complexity: O(1)

Find the most intervaled intervals
1. Sort the balloons by their end positions
2. Place arrows at the end of balloons,
which maximizes the chances of hitting other balloons
3. Count the minimum number of arrows needed

    case:
[1, 3], [1, 4], [2, 5] -> 1 arrow 3 balloons
    | arrow pos 1
    | we need to find a balloon that start pos > 3 to shoot another balloons

[1, 3], [1, 4], [2, 5], [4, 5]
                         | arrow pos 2
'''

from typing import List, Callable


class Solution:

    def findMinArrowShots(self, points) -> int:
        points.sort(key=lambda x: x[1])
        end_pos = points[0][1]
        arr = 1

        for s, e in points:
            if s > end_pos:
                arr += 1
                end_pos = e

        return arr


current_solution: Callable[[List[List[int]]], int] = None


def run_tests(input_file: str):
    global current_solution
    sol = Solution()

    #Change this to the function you want to test
    current_solution = sol.findMinArrowShots

    try:
        with open(input_file, 'r') as file:
            test_case = 1
            while True:
                #Read the number of points
                n = int(file.readline().strip())
                if n == 0:  # End of file
                    break

#Read the points
                points = []
                for _ in range(n):
                    point = list(map(int, file.readline().strip().split()))
                    points.append(point)


#Read the expected answer
                expected = int(file.readline().strip())

                result = current_solution(points)
                print(
                    f"Test Case {test_case}: {result}, {'Correct' if result == expected else 'Wrong'}"
                )

                test_case += 1

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_tests("452.txt")
