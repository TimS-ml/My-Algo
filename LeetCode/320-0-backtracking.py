'''
# Code Explain:
- Time complexity: O(n * 2^n)
- Space complexity: O(n)

# Pros and Cons and Notation:

'''


class Solution:
    def generateAbbreviations(self, word: str):
        # 'count' is count of consecutive abbreviated characters
        def backtrack(builder, pos, count):
            if pos == len(word):
                if count > 0:
                    builder += str(count)
                ans.append(builder)
            else:
                backtrack(builder, pos + 1, count + 1)
                # 这个track保证了index每次不断加1 从而在base的时候输出, 然后每一次count同时加1, 为了记录count
                backtrack(
                    builder + (str(count) if count > 0 else '') + word[pos],
                    pos + 1, 0)
                # 这个是为了退一步, 先保存当前的count数字, 然后因为数字不能连续, 所以+word [index], 同时把count清0

        ans = []
        backtrack('', 0, 0)
        return ans
