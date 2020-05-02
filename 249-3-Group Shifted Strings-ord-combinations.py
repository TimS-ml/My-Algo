# https://leetcode-cn.com/problems/group-shifted-strings/


from typing import List
import collections


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        n = len(strings)
        p = [i for i in range(n)]
        r = [0]*n
        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]
                
        def union(x,y):
            x,y = find(x),find(y)
            if r[x]>r[y]:
                p[y] = x
            else:
                p[x] = y
                if r[x] == r[y]:
                    r[y] += 1
                    
        for i,j in itertools.combinations(range(n),2):
            a,b = strings[i],strings[j]
            if len(a) == len(b):
                A,B = min(a,b),max(a,b)
                d = ord(B[0])-ord(A[0])
                if all((ord(A[i])-ord('a')+d)%26+ord('a') == ord(B[i]) for i in range(len(A))):
                    union(i,j)
        
        d = collections.defaultdict(list)
        for i in range(n):
            d[find(i)].append(strings[i])
        return list(map(list,d.values()))


# [["ayz"],["abc","bcd"]]
string = ["abc", "bcd", "ayz"]
print(Solution().groupStrings(string))

