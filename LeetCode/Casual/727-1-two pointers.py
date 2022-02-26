'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()



2 pointers
'''


class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        l1 = len(s1)
        l2 = len(s2)

        init = s1 + s2  # set a bigger value
        ans = init

        i = 0
        j = 0
        while i < l1:
            # char matched
            if s1[i] == s2[j]:
                j += 1

            # s2 all funded
            if j == l2:
                R = i  # right edge of ans
                j -= 1  # last char of s2
                while 0 <= j:  # find left edge
                    if s1[i] == s2[j]:
                        j -= 1
                    i -= 1
                i += 1

                # update if shorter answer found
                if (R - i + 1) < len(ans):
                    ans = s1[i:R + 1]
                # reset j
                j = 0

            # after `if j == l1`, i is located at the L side of ans
            #   where s1[i] == s2[0]
            i += 1

        return ans if ans != init else ''
