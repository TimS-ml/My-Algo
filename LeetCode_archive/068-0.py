'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''


class Solution:

    def fullJustify(self, words, maxWidth):
        ans, wordsWithExtraPadding, noSpaceWordsLen = [], [], 0
        for w in words:
            # print(ans, wordsWithExtraPadding, noSpaceWordsLen)
            if noSpaceWordsLen + len(w) + len(wordsWithExtraPadding) > maxWidth:
                # If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right
                for i in range(maxWidth - noSpaceWordsLen):
                    wordsWithExtraPadding[i % (len(wordsWithExtraPadding) - 1 or 1)] += ' '
                ans.append(''.join(wordsWithExtraPadding))
                wordsWithExtraPadding, noSpaceWordsLen = [], 0  # reset

            # non-terminate case
            wordsWithExtraPadding += [w]
            noSpaceWordsLen += len(w)
        return ans + [' '.join(wordsWithExtraPadding).ljust(maxWidth)]

    # Another way of writting it
    def fullJustify_2(self, words, maxWidth):
        ans, wordsWithExtraPadding, noSpaceWordsLen = [], [], 0
        for w in words:
            if noSpaceWordsLen + len(w) + len(wordsWithExtraPadding) > maxWidth:
                # single words case
                if len(wordsWithExtraPadding) == 1:
                    ans.append(wordsWithExtraPadding[0] + ' ' *
                               (maxWidth - noSpaceWordsLen))
                else:
                    numSpaces = maxWidth - noSpaceWordsLen
                    spaceBetweenWords, numExtraSpaces = divmod(
                        numSpaces,
                        len(wordsWithExtraPadding) - 1)  # note: - 1
                    # numExtraSpaces < wordsWithExtraPadding
                    for i in range(numExtraSpaces):
                        wordsWithExtraPadding[i] += ' '
                    ans.append((' ' * spaceBetweenWords).join(wordsWithExtraPadding))
                wordsWithExtraPadding, noSpaceWordsLen = [], 0
            
            # non-terminate case
            wordsWithExtraPadding += [w]
            noSpaceWordsLen += len(w)

        ans.append(' '.join(wordsWithExtraPadding) + ' ' *
                   (maxWidth - noSpaceWordsLen - len(wordsWithExtraPadding) + 1))
        return ans


words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16

print(Solution().fullJustify(words, maxWidth))
