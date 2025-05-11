'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(1)

case: ababcbaca
last_appear['a'] = 8
last_appear['b'] = 5
last_appear['c'] = 7

- init: s, e = 0, 0
- loc 0: s, e = 0, 8
- loc 1: s, e = 0, 8 (since last_appear['b] < 8)
...
- loc i: i == end, update s = end + 1
'''

from typing import List, Callable


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans = []
        last_appear = {}
        
        for i in range(len(s)):
            last_appear[s[i]] = max(i, last_appear.get(s[i], 0))
        
        start, end = 0, 0
        for i in range(len(s)):
            end = max(end, last_appear[s[i]])
            if i == end:
                ans.append(end - start + 1)
                start = end + 1

        return ans


current_solution: Callable[[str], List[int]] = None

def run_tests(input_file: str):
    global current_solution
    sol = Solution()

#Change this to the function you want to test
    current_solution = sol.partitionLabels

    try:
        with open(input_file, 'r') as file:
            test_case = 1
            while True:
#Read the input string
                s = file.readline().strip()
                if not s:  # End of file
                    break

#Read the expected answer
                expected_str = file.readline().strip()
                expected = list(map(int, expected_str.split(',')))
                
                result = current_solution(s)
                print(f"Test Case {test_case}: {result}, {'Correct' if result == expected else 'Wrong'}")
                
                test_case += 1

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_tests("763.txt")
