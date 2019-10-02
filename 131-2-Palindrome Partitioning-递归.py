# https://leetcode-cn.com/problems/palindrome-partitioning/


class Solution:
    def partition(self, s):
        split_result = []
        if len(s) == 0:
            return split_result

        def back(start=0, res=[]):
            if start >= len(s):
                split_result.append(res)
                return
            for end in range(start+1, len(s)+1):
                split_s = s[start:end]
                # 如果当前子串为回文串，则可以继续递归
                if split_s == s[start:end][::-1]:
                    back(end, res+[split_s])

        back()
        return split_result


s = 'aab'
print(Solution().partition(s))
