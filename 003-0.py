'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

combine hash and compare in one loop

Initialize Hash dict

[1] return a set
dic = {s[i] for i in range(len(s))}

[2] return a dict
dic = {}
start = 0
for i in range(len(s)):
    if s[i] in dic:
        start = dic[s[i]] + 1
    dic[s[i]] = i

# Pros and Cons:
## Pros:

## Cons:

# Notation:

'''
import collections


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        ans = 0
        start = 0

        for i in range(len(s)):
            if s[i] in dic and start <= dic[s[i]]:  # show up second time
                start = dic[s[i]] + 1
            else:
                ans = max(ans, i - start + 1)
            dic[s[i]] = i  # initialize
        return ans

    # same as sol 1
    def lengthOfLongestSubstring_2(self, s: str) -> int:
        dic = {}
        ans = 0
        start = 0

        for i in range(len(s)):
            if s[i] in dic:
                start = dic[s[i]] + 1
            dic[s[i]] = i

        for i in range(len(s)):
            ans = max(ans, i - start + 1)
        return ans

    def lengthOfLongestSubstring_3(self, s: str) -> int:
        d = collections.defaultdict(int)
        start = ans = 0
        for i, c in enumerate(s):
            while start > 0 and d[c] > 0:
                d[s[i - start]] -= 1
                start -= 1
            d[c] += 1
            start += 1
            ans = max(ans, start)
        return ans

    def lengthOfLongestSubstring_4(self, s: str) -> int:
        d = {}
        start = 0
        ans = 0
        for i, c in enumerate(s):
            if c in d:
                start = max(start, d[c] + 1)
            d[c] = i
            ans = max(ans, i - start + 1)
        return ans


s1 = "abcabc"
s2 = "pwwkew"  # wke
print(Solution().lengthOfLongestSubstring(s2))
