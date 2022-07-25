'''
# Code Explain:
- Time complexity: O(N * 2^N)
- Space complexity: O(N * 2^N)

lc 320
'''

from collections import deque


class AbbreviatedWord:

    def __init__(self, str, start, count):
        self.str = str
        self.start = start
        self.count = count


def generate_generalized_abbreviation(word):
    wordLen = len(word)
    result = []
    queue = deque()
    queue.append(AbbreviatedWord(list(), 0, 0))
    while queue:
        abWord = queue.popleft()
        if abWord.start == wordLen:
            if abWord.count != 0:
                abWord.str.append(str(abWord.count))
            result.append(''.join(abWord.str))
        else:
            # continue abbreviating by incrementing the current abbreviation count
            queue.append(
                AbbreviatedWord(list(abWord.str), abWord.start + 1,
                                abWord.count + 1))

            # restart abbreviating, append the count and the current character to the string
            if abWord.count != 0:
                abWord.str.append(str(abWord.count))

            newWord = list(abWord.str)
            newWord.append(word[abWord.start])
            queue.append(AbbreviatedWord(newWord, abWord.start + 1, 0))

    return result


def main():
    print("Generalized abbreviation are: " +
          str(generate_generalized_abbreviation("BAT")))
    print("Generalized abbreviation are: " +
          str(generate_generalized_abbreviation("code")))


main()
