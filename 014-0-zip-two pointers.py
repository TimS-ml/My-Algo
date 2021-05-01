# https://leetcode-cn.com/problems/longest-common-prefix/


class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if len(strs) == 0:
            return ""
        zipped = zip(*strs)
        ans = 0
        for i in zipped:
            print(i)
            if len(set(i)) != 1:
                return strs[0][:ans]
            ans += 1
        return strs[0][:ans]

    def longestCommonPrefix_2(self, strs) -> str:
        if len(strs) == 0:
            return ""
        ss = list(map(set, zip(*strs)))
        # [{'f'}, {'l', 'i'}, {'o', 'i', 'g'}, {'h', 'w', 'g'}]
        ans = ""
        for i, x in enumerate(ss):
            x = list(x)
            if len(x) > 1:
                break
            ans = ans + x[0]
        return ans

strs = ["cc", "c"]
# strs = ["flower", "flow", "flight"]
print(Solution().longestCommonPrefix(strs))
