'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''

class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        i = 0
        dic = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        
        rules = {
            'I': ['V', 'X'],
            'X': ['L', 'C'],
            'C': ['D', 'M']
        }
        
        while i < len(s):
            c = s[i]
            nxtC = None
            if i < len(s) - 1:  # has next char
                nxtC = s[i+1]
            
            if c in rules and nxtC in rules[c]:
                ans -= dic[c]
            else:
                ans += dic[c]
            
            i += 1
        
        return ans
