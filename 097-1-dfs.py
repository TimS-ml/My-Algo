'''
# Code Explain:
- Time complexity: O(n^2)
- Space complexity: O()

# Pros and Cons and Notation:

'''


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2, l3 = len(s1), len(s2), len(s3)
        if l1 + l2 != l3:
            return False

        cache = [[None for _ in range(l2 + 1)] for _ in range(l1 + 1)]

        def dfs(i, j):
            if cache[i][j] != None:
                return cache[i][j]

            if i + j == l3:
                return True

            ans = False
            if i < l1 and s1[i] == s3[i + j]:
                ans = dfs(i + 1, j)

            if j < l2 and s2[j] == s3[i + j]:
                # ans might already be True
                ans = ans or dfs(i, j + 1)

            cache[i][j] = ans
            return ans

        return dfs(0, 0)


s1 = "aabcce"
s2 = "dbbca"
s3 = "aadbbcbcace"
print(Solution().isInterleave(s1, s2, s3))
