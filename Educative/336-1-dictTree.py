'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

# Pros and Cons and Notation:

'''

class Node:
    def __init__(self):
        self.ch = [0] * 26
        self.flag = -1

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        tree = [Node()]

        def insert(s: str, index: int):
            length = len(s)
            add = 0
            for i in range(length):
                x = ord(s[i]) - ord("a")
                if tree[add].ch[x] == 0:
                    tree.append(Node())
                    tree[add].ch[x] = len(tree) - 1
                add = tree[add].ch[x]
            tree[add].flag = index
        
        def findWord(s: str, left: int, right: int) -> int:
            add = 0
            for i in range(right, left - 1, -1):
                x = ord(s[i]) - ord("a")
                if tree[add].ch[x] == 0:
                    return -1
                add = tree[add].ch[x]
            return tree[add].flag
        
        def isPalindrome(s: str, left: int, right: int) -> bool:
            length = right - left + 1
            return length < 0 or all(s[left + i] == s[right - i] for i in range(length // 2))
        
        n = len(words)
        for i, word in enumerate(words):
            insert(word, i)
        
        ans = list()
        for i, word in enumerate(words):
            m = len(word)
            for j in range(m + 1):
                if isPalindrome(word, j, m - 1):
                    leftId = findWord(word, 0, j - 1)
                    if leftId != -1 and leftId != i:
                        ans.append([i, leftId])
                if j and isPalindrome(word, 0, j - 1):
                    rightId = findWord(word, j, m - 1)
                    if rightId != -1 and rightId != i:
                        ans.append([rightId, i])

        return ans

