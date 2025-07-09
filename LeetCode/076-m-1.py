'''
# Code Explain:
- Time complexity: O(|S|+|T|)
    where |S| and |T| represent the lengths of strings S and T
- Space complexity: O(|S|+|T|)

reference state
dynamic state
'''

from typing import List, Callable
from collections import defaultdict


class Solution:
    # Array-based approach with char frequency tracking
    def minWindow(self, s: str, t: str) -> str:
        missing_cnt = defaultdict(int)
        window = defaultdict(int)

        for cr in t:
            missing_cnt[cr] += 1

        found = 0
        l = 0
        min_l = 0
        min_sz = len(s) + 1
        
        for r in range(len(s)):
            cr = s[r]

            if cr in missing_cnt:
                window[cr] += 1
                if window[cr] == missing_cnt[cr]: found += 1

            while found == len(missing_cnt):
                sz = r - l + 1
                cl = s[l]
                if sz < min_sz:
                    min_l = l
                    min_sz = sz

                # Remove leftmost char from window
                if cl in missing_cnt:
                    window[cl] -= 1
                    if window[cl] < missing_cnt[cl]:
                        found -= 1
                l += 1

        return "" if min_sz > len(s) else s[min_l: min_l+min_sz]


current_solution: Callable[[str, str], str] = None

def run_tests(input_file: str):
    global current_solution
    sol = Solution()
    
    # Change this to the function you want to test
    current_solution = sol.minWindow

    try:
        with open(input_file, 'r') as file:
            test_case = 1
            while True:
                n = int(file.readline().strip())
                if n == 0:
                    break
                
                s = file.readline().strip()
                t = file.readline().strip()
                expected = file.readline().strip()
                
                result = current_solution(s, t)
                print(f"Test Case {test_case}: '{result}', {'Correct' if result == expected else 'Wrong'}")
                
                test_case += 1

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_tests("076.txt")

