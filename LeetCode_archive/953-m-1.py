'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()


# Sol 1
case length match:
False:
apple
app

True:
app
apple

case skip compare:
appppp
apq
aprle

same as:
app
apq


# Implement
zip? no, it will lost length info unless we use padding(?)

use pointer


# Sol 2
map to english alphabet
'''

from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        idx_dic = {}
        for i in range(len(order)):
            idx_dic[order[i]] = i

        for i in range(len(words)-1):
            curr_w = words[i]
            next_w = words[i+1]
            for j in range(len(curr_w)):
                # same char, length match
                if j > len(next_w)-1:
                    return False

                # char match
                if idx_dic[curr_w[j]] > idx_dic[next_w[j]]:
                    return False
                elif idx_dic[curr_w[j]] < idx_dic[next_w[j]]:
                    break
        return True

    def isAlienSorted_2(self, words: List[str], order: str) -> bool:
        char_map = {c: i for i, c in enumerate(order)}

