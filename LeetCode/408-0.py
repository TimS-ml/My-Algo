'''
# Code Explain:
- Time complexity: O(N)
N = max(len(word), len(abbr))
- Space complexity: O(1)

We maintain two pointers, i pointing at word and j pointing at abbr.
There are only two scenarios:
- [a] j points to a letter. 
    We compare the value i and j points to. If equal, we increment them. Otherwise, return False.
- [b] j points to a digit. 
    We need to find out the complete number that j is pointing to, e.g. 123. 
    Then we would increment i by 123. We know that next we will:
    - either break out of the while loop if i or j is too large
    - or we will return to scenario [a]

'''


class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = j = 0
        while i < len(word) and j < len(abbr):
            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif abbr[j] == "0":
                return False
            elif abbr[j].isnumeric():
                dig = j
                while dig < len(abbr) and abbr[dig].isnumeric():
                    dig += 1
                # when j at first digit, i is at the first char of shortened string
                # apple  a3e
                #  |      |
                #  i      j
                # so it's i += num not i += num+1
                i += int(abbr[j:dig])
                j = dig
            else:
                return False
        return i == len(word) and j == len(abbr)  # this is important


word = "internationalization"
abbr = "i12iz4n"
print(Solution().validWordAbbreviation(word, abbr))
