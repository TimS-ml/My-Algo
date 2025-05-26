'''
# Code Explain:
- Time complexity: O(∣S∣+∣T∣)
    where |S| and |T| represent the lengths of strings S and T
- Space complexity: O(∣S∣+∣T∣)

'''

from typing import List, Callable
from collections import defaultdict
        


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # def char_to_index(c):
        #     # A-Z: 0-25, a-z: 26-51
        #     return ord(c) - ord('A') if c.isupper() else ord(c) - ord('a') + 26

        chars = [0] * 128
        need_chars = set()
        
        # 预处理target字符串
        for char in t:
            chars[ord(char)] += 1
            need_chars.add(ord(char))
        
        required = len(need_chars)
        formed = 0
        window_counts = [0] * 128
        
        left = right = 0
        min_len = float('inf')
        min_left = 0
        
        while right < len(s):
            char_code = ord(s[right])
            window_counts[char_code] += 1
            
            if char_code in need_chars and window_counts[char_code] == chars[char_code]:
                formed += 1
            
            while left <= right and formed == required:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_left = left
                
                left_char_code = ord(s[left])
                window_counts[left_char_code] -= 1
                if left_char_code in need_chars and window_counts[left_char_code] < chars[left_char_code]:
                    formed -= 1
                
                left += 1
            
            right += 1
        
        return "" if min_len == float('inf') else s[min_left:min_left + min_len]

    def minWindow_2(self, s: str, t: str) -> str:
        # 'need', no need to be a dict in this case
        need = dict() # char needed, unchange
        win = dict()  # window freq dict
        left, right = 0, 0

        valid = 0
        minStart, minLen = 0, float('inf')

        # hash init
        for char in t:
            need[char] = need.get(char, 0) + 1

        while right < len(s):
            c = s[right]
            right += 1

            if c in need:
                win[c] = win.get(c, 0) + 1
                if win[c] == need[c]:
                    valid += 1

            while valid == len(need):
                if right - left < minLen:
                    minStart = left
                    minLen = right - left

                # char to be delete
                d = s[left]
                left += 1

                if d in need:
                    if win[d] == need[d]:
                        valid -= 1
                    win[d] -= 1

        if minLen == float('inf'):
            return ''
        else:
            return s[minStart: minStart + minLen]

    def minWindow_3(self, s: str, t: str) -> str:
        need = defaultdict(int)
        for char in t:
            need[char] += 1
        
        missing = len(need)  # 需要匹配的不同字符数
        left = start = 0
        min_len = float('inf')
        
        for right, char in enumerate(s):
            if char in need:
                need[char] -= 1
                if need[char] == 0:
                    missing -= 1
            
            while missing == 0:
                if right - left + 1 < min_len:
                    start = left
                    min_len = right - left + 1
                
                if s[left] in need:
                    need[s[left]] += 1
                    if need[s[left]] == 1:
                        missing += 1
                left += 1
        
        return "" if min_len == float('inf') else s[start:start + min_len]

    # sol 3, but using loop edge as pointer
    def minWindow_3b(self, s: str, t: str) -> str:
        ans = ''
        dic = dict()  # freq dict of target char

        # hash init
        # dic[char] means number of char needed
        # when dic[char] <= 0, means the requirment satified
        for char in t:
            dic[char] = dic.get(char, 0) + 1

        left, right = 0, 0
        minLen = len(s)
        valid = 0

        while right < len(s):
            c = s[right]
            right += 1

            if c in dic:
                if dic[c] > 0:
                    valid += 1
                dic[c] -= 1

            while valid == len(t):
                if minLen >= right - left:
                    minLen = right - left
                    ans = s[left:right]

                # char to be delete
                d = s[left]
                if d in dic:
                    dic[d] += 1
                    if dic[d] > 0:
                        valid -= 1
                left += 1

        return ans


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
                # Read the length of string s
                n = int(file.readline().strip())
                if n == 0:  # End of file
                    break
                
                # Read string s
                s = file.readline().strip()
                
                # Read string t
                t = file.readline().strip()
                
                # Read the expected answer
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
