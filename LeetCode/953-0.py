'''
# Code Explain:
- Time complexity: O(M)  # M be the total number of characters in words.
- Space complexity: O(1)

The time complexity is tricky, since the len(alphabet) is fixed to 26

sol 1
Initialize a hashmap/array to record the relations between each letter and its ranking in order.
Iterate over words and compare each pair of adjacent words.
    Iterate over each letter to find the first different letter between words[i] and words[i + 1].
        If words[i + 1] ends before words[i] and no different letters are found, then we need to return false because words[i + 1] should come before words[i] (for example, apple and app).
        If we find the first different letter and the two words are in the correct order, then we can exit from the current iteration and proceed to the next pair of words.
        If we find the first different letter and the two words are in the wrong order, then we can safely return false.
If we reach this point, it means that we have examined all pairs of adjacent words and that they are all sorted. Therefore we can return true.


sol 2
Another way to think map alphabet to number:
    map 'xyz' to '123' is the same as map alphabet back to English ('xyz' to 'abc')

We can replace words into idx numbers

A correct way to use zip for two words comparison
zip(words_en_idx, words_en_idx[1:])

case:
["hello","leetcode"]
"hlabcdefgijkmnopqrstuvwxyz"

words_en_idx
[[0, 6, 1, 1, 14], [1, 6, 6, 19, 4, 14, 5, 6]]
'''

from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        idx_dic = {}
        for index, val in enumerate(order):
            idx_dic[val] = index
        
        # i: idx of a word
        # j; idx of a char in word[i]
        for i in range(len(words) - 1):
            for j in range(len(words[i])):
                # no mismatch, examine length
                if j >= len(words[i + 1]):
                    return False
                
                # mismatch
                if words[i][j] != words[i + 1][j]:
                    if idx_dic[words[i][j]] > idx_dic[words[i + 1][j]]:
                        return False
                    # if we find the first different character and they are sorted,
                    # then there's no need to check remaining letters
                    break

        return True

    def isAlienSorted_2(self, words: List[str], order: str) -> bool:
        idx_dic = {c: i for i, c in enumerate(order)}
        words_en_idx = []
        for w in words:
            words_en_idx.append([idx_dic[c] for c in w])

        return all(w1 <= w2 for w1, w2 in zip(words_en_idx, words_en_idx[1:]))
