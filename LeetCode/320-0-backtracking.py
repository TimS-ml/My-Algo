'''
# Code Explain:
- Time complexity: O(n * 2^n)
- Space complexity: O(n)

'''


class Solution:
    def generateAbbreviations(self, word: str):
        # 'count' is count of consecutive abbreviated characters
        def backtrack(subStr, pos, count):
            if pos == len(word):
                if count > 0:
                    subStr += str(count)
                ans.append(subStr)
            else:
                # keep using num abbr: w=apple, a2 + l => a3 / app + l => app1
                backtrack(subStr, pos + 1, count + 1)

                # not using num abbr: w=apple, a2 + l => a2l / app + l => appl
                backtrack(
                    subStr + (str(count) if count > 0 else '') + word[pos],
                    pos + 1, 0)

        ans = []
        backtrack('', 0, 0)
        return ans
