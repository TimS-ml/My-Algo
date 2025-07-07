'''
# Code Explain:
- Time complexity: O(|S|+|T|)
    where |S| and |T| represent the lengths of strings S and T
- Space complexity: O(|S|+|T|)
'''

from typing import List, Callable
from collections import defaultdict


class Solution:
    # Array-based approach with char frequency tracking
    def minWindow(self, s: str, t: str) -> str:
        chars = [0] * 128  # target char frequency array
        need = set()       # set of target char codes
        
        # Initialize target character requirements
        for char in t:
            chars[ord(char)] += 1
            need.add(ord(char))
        
        required = len(need)       # number of unique chars needed
        formed = 0                 # number of unique chars satisfied
        window_counts = [0] * 128  # current window char frequency
        
        left = right = 0
        min_len = float('inf')
        min_start = 0
        
        while right < len(s):
            char_code = ord(s[right])
            window_counts[char_code] += 1
            
            # Check if frequency requirement is satisfied for this char
            if char_code in need and window_counts[char_code] == chars[char_code]:
                formed += 1
            
            # Contract window when all requirements are met
            while left <= right and formed == required:
                # Update minimum window if current is smaller
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_start = left
                
                # Remove leftmost char from window
                left_char_code = ord(s[left])
                window_counts[left_char_code] -= 1
                if left_char_code in need and window_counts[left_char_code] < chars[left_char_code]:
                    formed -= 1
                
                left += 1
            
            right += 1
        
        return "" if min_len == float('inf') else s[min_start:min_start + min_len]

    # Dictionary-based approach with valid counter
    def minWindow_2(self, s: str, t: str) -> str:
        need = dict()              # target char frequency dict
        window = dict()            # current window char frequency dict
        left = right = 0
        
        valid = 0                  # number of unique chars with satisfied frequency
        min_start = 0
        min_len = float('inf')

        # Initialize target character requirements
        for char in t:
            need[char] = need.get(char, 0) + 1

        while right < len(s):
            char = s[right]
            right += 1

            # Expand window: add current char to window
            if char in need:
                window[char] = window.get(char, 0) + 1
                if window[char] == need[char]:
                    valid += 1

            # Contract window when all requirements are met
            while valid == len(need):
                # Update minimum window if current is smaller
                if right - left < min_len:
                    min_start = left
                    min_len = right - left

                # Remove leftmost char from window
                char_to_remove = s[left]
                left += 1

                if char_to_remove in need:
                    if window[char_to_remove] == need[char_to_remove]:
                        valid -= 1
                    window[char_to_remove] -= 1

        return "" if min_len == float('inf') else s[min_start:min_start + min_len]

    # DefaultDict approach with missing counter
    def minWindow_3(self, s: str, t: str) -> str:
        need = defaultdict(int)    # target char frequency dict
        
        # Initialize target character requirements
        for char in t:
            need[char] += 1
        
        missing = len(need)        # number of unique chars still needed
        left = 0
        min_start = 0
        min_len = float('inf')
        
        # Expand window using enumeration
        for right, char in enumerate(s):
            # Add current char to window
            if char in need:
                need[char] -= 1
                if need[char] == 0:    # requirement satisfied for this char
                    missing -= 1
            
            # Contract window when all requirements are met
            while missing == 0:
                # Update minimum window if current is smaller
                if right - left + 1 < min_len:
                    min_start = left
                    min_len = right - left + 1
                
                # Remove leftmost char from window
                if s[left] in need:
                    need[s[left]] += 1
                    if need[s[left]] == 1:    # requirement no longer satisfied
                        missing += 1
                left += 1
        
        return "" if min_len == float('inf') else s[min_start:min_start + min_len]

    # Alternative dict approach using total character count
    def minWindow_4(self, s: str, t: str) -> str:
        need = dict()              # target char frequency dict
        left = right = 0
        min_len = len(s) + 1
        min_start = 0
        
        valid = 0                  # total number of chars satisfied (not unique)

        # Initialize target character requirements
        for char in t:
            need[char] = need.get(char, 0) + 1

        while right < len(s):
            char = s[right]
            right += 1

            # Expand window: add current char
            if char in need:
                if need[char] > 0:     # only count if still needed
                    valid += 1
                need[char] -= 1

            # Contract window when all chars are satisfied
            while valid == len(t):
                # Update minimum window if current is smaller
                if min_len >= right - left:
                    min_len = right - left
                    min_start = left

                # Remove leftmost char from window
                char_to_remove = s[left]
                if char_to_remove in need:
                    need[char_to_remove] += 1
                    if need[char_to_remove] > 0:    # becomes needed again
                        valid -= 1
                left += 1

        return "" if min_len > len(s) else s[min_start:min_start + min_len]


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

