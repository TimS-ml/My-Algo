'''
2 pointers

False
word = "apple", abbr = "a2e"

word = "appee", abbr = "a2e"
'''

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        p1, p2 = 0, 0
        while p1 < len(word), p2 < len(abbr):
            if abbr[p2].isdigit():
                if abbr[p2] == 0:  # no edge here?
                    return False
                dig = 0
                while abbr[p2].isdigit() and p2 < len(abbr):
                    p2 += 1
                    dig = abbr[p2] + dig * 10

                p1 += dig
