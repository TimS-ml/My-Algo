'''
a list of words
len of word < 20
len(order)==26
lower case? Yes
Can I Mod input list? sure.

BF
2 by 2 comparison, 2 pointers

Sol
- zip
- lex within each zip set
- list and get index function

case:
shortest
"hellolee"
"helloleetcode"

case:
"apple"
"aqp"
"aqz"

case:
"apple"
"b"

Feedback
- compare adjacent words is correct
- zip is an elegant but not suitable approach
- make sure which type of hash dict are you using (by idx or by freq)
- you know every tricky part, but how to aggregrate them together
'''

from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # order = list(order)
        dic = {}
        for char in range(len(order)):
            dic[char] = dic.get(char, 0) + 1

        zip_words = zip(*words)   # space ???

        start_idx = 0
        for char_set in zip_words:
            i = start_idx
            while i < len(char_set)-2:  # check edge
                if char_set[i] == char_set[i+1]:
                    i += 1
                else:
                    if dic(char_set[i]) < dic(char_set[i+1]):
                        start_idx += 1
                        i += 1
                    else:
                        return False

        return True

    # a better but still failed solution
    def isAlienSorted_2(self, words: List[str], order: str) -> bool:
        dic = {}

        # WRONG: not a freq dict!!!
        for i in range(len(order)):
            char = order[i]
            dic[char] = dic.get(char, 0) + 1

        zip_words = zip(*words)
        if len(words) == 2:
            for char_set in zip_words:
                if dic[char_set[0]] > dic[char_set[1]] and last_dig_align:
                    return False

            if len(words[0]) > len(words[1]):
                return False
        else:
            for char_set in zip_words:
                i = 0  # idx of a len=2 sliding window
                while i < len(char_set) - 2:  # check edge
                    if dic[char_set[i]] < dic[char_set[i+1]]:
                        i += 1
                    else:
                        return False

            for i in range(len(words)-1):
                if len(words[i]) > len(words[i+1]) and last_dig_align:
                    return False
        return True

