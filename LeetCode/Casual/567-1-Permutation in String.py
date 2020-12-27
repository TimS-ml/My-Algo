# https://leetcode-cn.com/problems/permutation-in-string/


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # O(n)
       dic1, dic2 = dict(), dict()
       for s in s1:
           dic1[s] = dic1.get(s, 0) + 1
        start, end = 0, 0

        while end < len(s2):
            dic2[s2[end]] = dic2.get(s2[end], 0) + 1
            if dic1 == dic2:
                return True
            end += 1

            # compare
            if end - start + 1 > len(s1):
                dic2[s2[start]] -= 1
                if dic2[s2[start]] == 0:
                    del(dic2[s2[start]])
                start += 1

        return False
