# https://leetcode-cn.com/problems/longest-substring-with-at-least-k-repeating-characters/
# Divide-and-conquer_algorithm
# At least就表明至少有那么多，用字典就不太好使了


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        # 按照count排序 Note: c = min(s, key=s.count) can be very slow
        c = min(set(s), key=s.count)
        print('c:', c)
        if s.count(c) >= k:
            print('>=', c, s.count(c))
            return len(s)
        return max(self.longestSubstring(t, k) for t in s.split(c))


s = "ababbc"
k = 2
# print(s.split('c'))
print(Solution().longestSubstring(s, k))
