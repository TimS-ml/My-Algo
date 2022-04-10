'''
# Code Explain:
N is the length of strs, and K is the maximum length of a string in strs

sol 1
- Time complexity: O(NK logK)
- Space complexity: O(NK)

- Time complexity: O(NK)
- Space complexity: O(NK)
'''

import collections


class Solution:
    # Categorize by Sorted String
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()

    def groupAnagrams_2(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            # speed up: avoid using sort
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()
