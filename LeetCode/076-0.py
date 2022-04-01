'''
# Code Explain:
- Time complexity: O(∣S∣+∣T∣) 
    where |S| and |T| represent the lengths of strings S and T
- Space complexity: O(∣S∣+∣T∣)

'''

import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dic = dict()  # target freq dict, unchange after init
        win = dict()  # window freq dict
        left, right = 0, 0

        valid = 0
        minStart, minLen = 0, float('inf')

        # hash init
        for char in t:
            dic[char] = dic.get(char, 0) + 1

        while right < len(s):
            c = s[right]
            right += 1

            if c in dic:
                win[c] = win.get(c, 0) + 1
                if win[c] == dic[c]:
                    valid += 1

            while valid == len(dic):
                if right - left < minLen:
                    minStart = left
                    minLen = right - left

                # char to be delete
                d = s[left]
                left += 1

                if d in dic:
                    if win[d] == dic[d]:
                        valid -= 1
                    win[d] -= 1

        if minLen == float('inf'):
            return ''
        else:
            return s[minStart: minStart + minLen]

    
    # using fewer var
    def minWindow_2(self, s: str, t: str) -> str:
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


# Output: "BANC"
S = "ADOBECODEBANC"
T = "AABC"  # this will not trigger the while loop
# T = "ABC"
print(Solution().minWindow(S, T))
