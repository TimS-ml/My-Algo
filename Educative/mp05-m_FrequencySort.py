'''
# Code Explain:
- Time complexity: O(N + DlogD)
    where D is the number of distinct characters in the input string
- Space complexity: O(N)

lc 451
'''

import collections


def sort_character_by_frequency(s):
    # O(N)
    counts = collections.Counter(s)
    
    # Build up the string builder.
    string_builder = []
    for letter, freq in counts.most_common():
        # letter * freq makes freq copies of letter.
        # e.g. "a" * 4 -> "aaaa"
        string_builder.append(letter * freq)
    return ''.join(string_builder)


def main():

    print("String after sorting characters by frequency: " +
          sort_character_by_frequency("Programming"))
    print("String after sorting characters by frequency: " +
          sort_character_by_frequency("abcbab"))


main()
