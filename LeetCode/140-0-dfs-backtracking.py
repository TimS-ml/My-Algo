'''
# Code Explain:
- Time complexity: O(N^2 + 2^N + W)
- Space complexity: O(2^N x N + W)

case
'catsanddog'
['cat','cats','and','sand','dog']

memo
{'dog': [['dog']], 'sanddog': [['sand', 'dog']], 'catsanddog': [['cat', 'sand', 'dog'], ['cats', 'and', 'dog']], 'anddog': [['and', 'dog']]}
we only want memo['catsanddog']
'''

from collections import defaultdict

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        # table to map a string to its corresponding words break
        # {string: [['word1', 'word2'...], ['word3', 'word4', ...]]}
        memo = defaultdict(list)

        #@lru_cache(maxsize=None)    # alternative memoization solution
        # func(path, search space) -> subsentence (the solution of this subStr)
        # in this case, path is sub string of s, search space is fixed
        # {'dog': [['dog']], 'sanddog': [['sand', 'dog']],
        #  'catsanddog': [['cat', 'sand', 'dog'], ['cats', 'and', 'dog']],
        #  'anddog': [['and', 'dog']]}
        def helper(subStr):
            if not subStr:
                return [[]]  # list of empty list

            # multiple path can lead to the same substring
            # case: s = 'catdogcatdog'
            if subStr in memo:
                return memo[subStr]

            # s = 'catsanddog', wordDict = ['cat','cats','and','sand','dog', 's', 'andd', 'og']
            # the very first recursion will pick
            #   'cat' + helper('sanddog')
            #   = 'cat' + ['sand', 'dog'] or ['s', 'andd', 'og']
            #   'cats' + helper('anddog')
            #   ...
            for endIndex in range(1, len(subStr)+1):
                word = subStr[:endIndex]
                if word in wordSet:
                    # move forwards to break the postfix into words
                    for subsentence in helper(subStr[endIndex:]):
                        memo[subStr].append([word] + subsentence)

            return memo[subStr]

        helper(s)

        # chain up the lists of words into sentences.
        return [' '.join(words) for words in memo[s]]
