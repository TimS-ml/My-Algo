# https://leetcode-cn.com/problems/partition-labels/


class Solution:
    def partitionLabels(self, S: str):
        # the last time each letters show up
        last = {}
        for i, letter in enumerate(S):
            last[letter] = i
        print(last)

        ans = []
        cur = last[S[0]]

        for i, c in enumerate(S):
            # update cur like a sliding window
            if last[c] > cur:
                cur = last[c]
            if i == cur:
                ans.append(cur + 1 - sum(ans))
            print(i, c, cur, ans)
        return ans


S = "ababcbacadefegdehijhklij"
print(Solution().partitionLabels(S))
