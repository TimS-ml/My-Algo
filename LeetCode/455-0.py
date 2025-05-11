'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''

from typing import List, Callable


class Solution:

    def findContentChildren(self, g, s) -> int:
        g.sort()  # kids
        s.sort()  # cookies
        i = 0
        for cookie in s:
            if i >= len(g):
                break
            if g[i] <= cookie:
                i += 1
        return i


current_solution: Callable[[List[int], List[int]], int] = None


def run_tests(input_file: str):
    global current_solution
    sol = Solution()

    # Change this to the function you want to test
    current_solution = sol.findContentChildren

    try:
        with open(input_file, 'r') as file:
            test_case = 1
            while True:
                in1 = list(map(int, file.readline().strip().split()))
                in2 = list(map(int, file.readline().strip().split()))
                ans = list(map(int, file.readline().strip().split()))

                if not in1 and not in2 and not ans:
                    break

                result = current_solution(in1, in2)
                print(
                    f"Test Case {test_case}: {result}, {'Correct' if result == ans[0] else 'Wrong'}"
                )

                test_case += 1

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    run_tests("455.txt")
