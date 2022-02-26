'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()



'''
import functools


class Solution:
    @functools.lru_cache(None)
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1 or not word2:
            return len(word1) + len(word2)
        if word1[0] == word2[0]:
            return self.minDistance(word1[1:], word2[1:])
        else:
            inserted = 1 + self.minDistance(word1, word2[1:])
            deleted = 1 + self.minDistance(word1[1:], word2)
            replace = 1 + self.minDistance(word1[1:], word2[1:])
            return min(inserted, deleted, replace)
