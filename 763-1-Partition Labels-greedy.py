# https://leetcode-cn.com/problems/partition-labels/


class Solution:
    def partitionLabels(self, S: str):
        dic = {}
        for i, letter in enumerate(S):
            dic[letter] = i
        res = []
        cur = dic[S[0]]
        print(dic, cur)

        for i, letter in enumerate(S):
            if dic[letter] > cur:
                cur = dic[letter]  # update paragraph
            if i == cur:
                res.append(cur+1-sum(res))
        return res


S = "ababcbacadefegdehijhklij"
print(Solution().partitionLabels(S))
