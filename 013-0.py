'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

XLIX = 49
[1] 10
[2] 10 + 50 and 50 > 10
[3] 10 + 50 - 2*10 = 40
[4] 40 + 1
[5] 40 + 1 + 10 and 10 > 1
[6] 40 + 1 + 10 - 2*1


# Pros and Cons:
## Pros:

## Cons:

# Notation:
    I - 1
    V - 5
    X - 10
    L - 50
    C - 100
    D - 500
    M - 1000
'''



class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        prev, ans = dic[s[0]], dic[s[0]]

        if len(s) == 1:
            return ans

        for i in range(1, len(s)):
            curr = dic[s[i]]
            ans += curr
            if curr > prev:
                ans -= 2 * prev
            prev = curr
        return ans

    # This (seems) faster
    def romanToInt_2(self, s: str) -> int:
        dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        ans = 0
        
        # Or return ans if you choose this
        # for i, n in enumerate(s):
        #     if i < len(s)-1 and dic[s[i]] < dic[s[i+1]]:
        #         ans -= dic[s[i]]
        #     else:
        #         ans += dic[s[i]]

        for i in range(len(s) - 1):
            if dic[s[i]] < dic[s[i+1]]:
                ans -= dic[s[i]]
            else:
                ans += dic[s[i]]

        return ans + dic[s[-1]]


s = "MCMXCI"  # 1994.M+CM+XC+IV = +1000 (-100 +1000) (-10 +100) (-1 +5)
print(Solution().romanToInt(s))
