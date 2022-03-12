'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''

class Solution:

    @lru_cache(maxsize=None)
    def recursiveWithMemo(self, index, s) -> int:
        # ==len and len-1 make sure idx+2 will not out of boundary

        # If you reach the end of the string
        # Return 1 for success.
        if index == len(s):
            return 1

        # Last digit
        if index == len(s)-1:
            return 1

        # If the string starts with a zero, it can't be decoded
        if s[index] == '0':
            return 0
    
        answer = self.recursiveWithMemo(index + 1, s)
        if int(s[index : index + 2]) <= 26:
            answer += self.recursiveWithMemo(index + 2, s)

        return answer

    def numDecodings(self, s: str) -> int:
        return self.recursiveWithMemo(0, s)
