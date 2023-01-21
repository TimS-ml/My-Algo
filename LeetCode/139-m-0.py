'''
# Code Explain:
TLE solution
- Time complexity: O(2^N)
- Space complexity: O(N)

- reuse
- use only part of the dict

cache is a list of False, telling you we can't success starting this idx
'''

from typing import List
from collections import deque


class Solution:
    # TLE
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def helper(idx):
            if idx > len(s):
                return False
            if idx == len(s):
                return True
            # do the check
            for w in wordDict:
                # continue check
                if s[idx:idx + len(w)] == w:
                    # print(s[idx: idx + len(w)], w)
                    if helper(idx + len(w)):
                        return True
            return False

        return helper(0)

    # let mod this to a AC solution
    # we were calling the recursive function multiple times for a particular string
    def wordBreak_mod(self, s: str, wordDict: List[str]) -> bool:
        cache = {}
        def helper(start):
            if start == len(s):
                return True
            if start in cache:
                return cache[start]  # False
            for end in range(start + 1, len(s) + 1):
                if s[start: end] in wordDict:
                    if helper(end):
                        # cache[end] = True
                        return True
            cache[start] = False
            return False

        return helper(0)

    # further optimize
    def wordBreak_mod2(self, s: str, wordDict: List[str]) -> bool:
        cache = {}
        endIdx = [len(w) for w in wordDict]
        dictSet = set(wordDict)

        def helper(start):
            if start == len(s):
                return True
            if start in cache:
                return cache[start]  # False
            for wordLen in endIdx:
                end = start + wordLen
                if s[start: end] in dictSet:
                    if helper(end):
                        # cache[end] = True
                        return True
            cache[start] = False
            return False

        return helper(0)

    # bfs
    def wordBreak_mod3(self, s: str, wordDict: List[str]) -> bool:
        visited = set()  # visited = cache
        endIdx = [len(w) for w in wordDict]
        dictSet = set(wordDict)
        q = deque()
        q.append(0)  # helper(0)

        while q:
            start = q.popleft()

            if start == len(s):
                return True
            
            # same as cache
            if start not in visited:
                visited.add(start)

                for wordLen in endIdx:
                    end = start + wordLen
                    if s[start: end] in dictSet:
                        q.append(end)
        return False
    
    # quite samilar
    # dp[i] = can be segmented for s[:i]
    def wordBreak_mod4(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True

        # visited = set()  # visited = cache
        # endIdx = [len(w) for w in wordDict]
        dictSet = set(wordDict)

        for end in range(1, len(s) + 1):
            for start in range(end):
                if s[start:end] in dictSet:
                    dp[end] = dp[start]
                    if dp[end] == True:
                        break
        return dp[-1]



s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
wordDict = [
    "a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa",
    "aaaaaaaaa", "aaaaaaaaaa"
]
