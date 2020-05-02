# https://leetcode-cn.com/problems/group-shifted-strings/


from typing import List
import collections


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        def is_shift(s1, s2):
            dist = (ord(s1[0])-ord(s2[0])+26)%26
            for i,j in zip(s1, s2):
                cur_dist = (ord(i)-ord(j)+26)%26
                if dist!=cur_dist: return False
            return True
        
        d = defaultdict(dict)
        for s in strings:
            if not d[len(s)]:
                d[len(s)][s] = [s]
            else:
                flag = 0
                for k in d[len(s)]:
                    if is_shift(k, s): 
                        d[len(s)][k].append(s)
                        flag = 1
                        break
                if not flag: d[len(s)][s] = [s]
        
        res = []
        for group_dict in d.values():
            for group_list in group_dict.values():
                res.append(group_list)
        return res


# [["ayz"],["abc","bcd"]]
string = ["abc", "bcd", "ayz"]
print(Solution().groupStrings(string))

