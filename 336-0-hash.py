'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

# Pros and Cons and Notation:
- len(word1) == len(word2)
    - check word1 == word2[::-1]
- len(word1) != len(word2) 2 Possibility:
    - len(word1) > len(word2)
        - word1 = flip + palindrome, word2 = flip
        - case: bba and a => abba
            - palindrome is bb
    - len(word1) < len(word2)
        - word2 = flip + palindrome, word1 = flip
'''

from typing import List


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def findWord(s: str, left: int, right: int) -> int:
            return indices.get(s[left:right + 1], -1)

        def isPalindrome(s: str, left: int, right: int) -> bool:
            # return (sub := s[left:right + 1]) == sub[::-1]
            sub = s[left:right + 1]
            return sub == sub[::-1]

        # n = len(words)
        indices = {w[::-1]: i for i, w in enumerate(words)}

        ans = list()
        for i, w in enumerate(words):
            m = len(w)
            for j in range(m + 1):
                if isPalindrome(w, j, m - 1):
                    leftId = findWord(w, 0, j - 1)
                    if leftId != -1 and leftId != i:
                        ans.append([i, leftId])
                if j and isPalindrome(w, 0, j - 1):
                    rightId = findWord(w, j, m - 1)
                    if rightId != -1 and rightId != i:
                        ans.append([rightId, i])
        return ans

    def palindromePairs_2(self, words: List[str]) -> List[List[int]]:
        ans = []
        worddict = {w: i for i, w in enumerate(words)}
        for i, w in enumerate(words):
            for j in range(len(w)+1): 
                # 这里+1是因为，列表切片是前闭后开区间
                tmp1 = w[:j]  # 字符串的前缀
                tmp2 = w[j:]  # 字符串的后缀
                if tmp1[::-1] in worddict and worddict[tmp1[::-1]] != i and tmp2 == tmp2[::-1]:
                    # 当w的前缀在字典中+不是w自身+w剩下部分是回文(空也是回文)
                    ans.append([i, worddict[tmp1[::-1]]])  # 返回此时的w下标和找到的字符串下标

                if j > 0 and tmp2[::-1] in worddict and worddict[tmp2[::-1]] != i and tmp1 == tmp1[::-1]:         
                    # 当w的后缀在字典中+不是w自身+w剩下部分是回文(空也是回文)
                    # 注意: 因为是后缀,所以至少要从w的第二位算起,所以j>0
                    ans.append([worddict[tmp2[::-1]], i])  # 返回此时的w下标和找到的字符串下标
        return ans
