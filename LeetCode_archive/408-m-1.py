'''
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(1)

2 pointers

i for word
j for abbr

if number
    if 0
        false
    find whole numbers (j)
        end of dig?
    move i
if dig
    check if same

edge case:
s99n
0
4 valid

cat -> end of loop
3

"internationalization"
"i5a11o1"
'''

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0
        while i < len(word) and j < len(abbr):
            if abbr[j].isdigit():
                if abbr[j] == '0':  # check
                    return False
                num = 0
                while j < len(abbr) and abbr[j].isdigit():  # check
                    num = int(abbr[j]) + num * 10  # check
                    j += 1
                i += num
            else:
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1

        return i == len(word) and j == len(abbr)
