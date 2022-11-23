'''
# Code Explain:
- Time complexity: O(M+N)
- Space complexity: O(M+N)

'''

class Solution:
    def intervalIntersection(self, l1: List[List[int]], l2: List[List[int]]) -> List[List[int]]:
        ans = []

        i, j = 0, 0
        while i < len(l1) and j < len(l2):
            a1, a2 = l1[i][0], l1[i][1]
            b1, b2 = l2[j][0], l2[j][1]

            if b2 >= a1 and a2 >= b1:
                ans.append([max(a1, b1), min(a2, b2)])
            if b2 < a2:
                j += 1
            else:
                i += 1
        return ans
