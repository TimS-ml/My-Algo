'''
# Code Explain:
- Time complexity: O(N^3)
- Space complexity: O(N)

if w in wordDict == s[:len(w)], check rest of the s[len(w):]
'''

from typing import List
import functools


class Solution:
    # backtrack
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @functools.lru_cache(None)
        def backtrack(substr):
            if (not substr):
                return True
            ans = False
            for i in range(1, len(substr) + 1):
                if (substr[:i] in wordDict):
                    ans = backtrack(substr[i:]) or ans
            return ans

        return backtrack(s)

    # bfs
    def wordBreak_2(self, s, wordDict):
        queue = [0]
        len_list = [l for l in set(map(len, wordDict))]
        visited = [0 for _ in range(len(s) + 1)]
        while queue:
            start = queue.pop(0)
            for l in len_list:
                if s[start:start + l] in wordDict:
                    if start + l == len(s):  # segment exactly
                        return True
                    if visited[start + l] == 0:
                        # queue.pop(0)+l so that they can continue
                        queue.append(start + l)
                        visited[start + l] = 1
        return False


# False
s = "catsandog"
w = ["cats", "dog", "sand", "and", "cat"]

# True
s = "catsandog"
w = ["cats", "og", "sand", "and", "cat"]

# # True
# s = "applepenapple"
# w = ["apple", "pen"]

# # True
# s = "appenapp"
# w = ["ap", "pen", "app"]

print(Solution().wordBreak(s, w))
