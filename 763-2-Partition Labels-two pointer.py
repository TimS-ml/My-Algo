# https://leetcode-cn.com/problems/partition-labels/


class Solution:
    def partitionLabels(self, S: str):
        # the last time each letters show up
        last = {c: i for i, c in enumerate(S)}
        print(last)

        ans = []
        cur = anchor = 0

        for i, c in enumerate(S):
            # update cur like a sliding window
            cur = max(cur, last[c])
            if i == cur:
                ans.append(i + 1 - anchor)
                anchor = i + 1
            print(i, c, cur, ans)
        return ans


S = "ababcbacadefegdehijhklij"
print(Solution().partitionLabels(S))
