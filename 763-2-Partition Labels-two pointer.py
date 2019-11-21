# https://leetcode-cn.com/problems/partition-labels/


class Solution:
    def partitionLabels(self, S: str):
        # the last time each letters show up
        last = {c: i for i, c in enumerate(S)}
        print(last)
        j = anchor = 0
        ans = []
        for i, c in enumerate(S):
            # update j like a sliding window
            j = max(j, last[c])
            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1
            print(i, c, j, ans)
        return ans


S = "ababcbacadefegdehijhklij"
print(Solution().partitionLabels(S))

