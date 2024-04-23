'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

case: 'abcabcbb'
       |
     start = 0
[1]   s[i] = 'a' and dic = {'a': 0}, update ans = 1
[2-3] i -> c, updated dic = {'a': 0, 'b': 1, 'c': 2}, update ans = 3
[4]   s[i] = 'a' and dic = {'a': 3, 'b': 1, 'c': 2}, update ans still = 3
[5]   'abcabcbb'
        |
     new start = old start + 1
               = 0 + 1

'''
import collections

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        ans = 0
        win = dict()  # window freq dict

        while right < len(s):
            c = s[right]
            right += 1

            win[c] = win.get(c, 0) + 1

            while win[c] > 1:
                d = s[left]
                left += 1
                win[d] -= 1

            ans = max(ans, right - left)

        return ans

    def lengthOfLongestSubstring_2(self, s: str) -> int:
        dic = {}
        ans = 0
        start = 0

        for i in range(len(s)):
            # update start point if duplicate
            # why don't remove start <= dic[s[i]] ?
            # case: "tmmzuxt"
            #          |   |
            #       start [t in dic]
            # in this case, if we update start, it will go backwords
            if s[i] in dic and start <= dic[s[i]]:
                start = dic[s[i]] + 1
            else:
                ans = max(ans, i - start + 1)
            dic[s[i]] = i  # save the position to dict
        return ans

    def lengthOfLongestSubstring_3(self, s: str) -> int:
        dic = {}
        ans = 0
        start = 0

        for i, c in enumerate(s):
            if c in dic:
                start = max(start, dic[c] + 1)
            # don't ans = max() in else! or you will miss
            # s[i] in dic and start > dic[s[i]] case
            ans = max(ans, i - start + 1)
            dic[c] = i
        return ans

    # this is close to sol 1
    def lengthOfLongestSubstring_4(self, s: str) -> int:
        dic = collections.defaultdict(int)
        ans = 0
        length = 0

        for i, c in enumerate(s):
            while length > 0 and dic[c] > 0:
                dic[s[i - length]] -= 1
                length -= 1
            dic[c] += 1
            length += 1
            ans = max(ans, length)
        return ans


s1 = "abcabc"
s2 = "pwwkew"  # wke
s3 = "abcabcbb"
print(Solution().lengthOfLongestSubstring_2(s3))
