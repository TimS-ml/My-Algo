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
map alphabet back to English
'''

from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {}
        for index, val in enumerate(order):
            order_map[val] = index

        for i in range(len(words) - 1):
            for j in range(len(words[i])):
                # If we do not find a mismatch letter between words[i] and words[i + 1],
                # we need to examine the case when words are like ("apple", "app").
                if j >= len(words[i + 1]): return False

                if words[i][j] != words[i + 1][j]:
                    if order_map[words[i][j]] > order_map[words[i + 1][j]]: return False
                    # if we find the first different character and they are sorted,
                    # then there's no need to check remaining letters
                    break

        return True

    def isAlienSorted_2(self, words: List[str], order: str) -> bool:
        m = {c: i for i, c in enumerate(order)}
        words = [[m[c] for c in w] for w in words]
        return all(w1 <= w2 for w1, w2 in zip(words, words[1:]))
