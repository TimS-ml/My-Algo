from collections import deque


class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))

    def reverseWords_2(self, s: str) -> str:
        left, right = 0, len(s) - 1

        while left <= right and s[left] == ' ':
            left += 1

        while left <= right and s[right] == ' ':
            right -= 1

        d, word = deque(), []
        while left <= right:
            if s[left] == ' ' and word:
                d.appendleft(''.join(word))
                word = []
            elif s[left] != ' ':
                word.append(s[left])
            left += 1
        d.appendleft(''.join(word))

        return ' '.join(d)
