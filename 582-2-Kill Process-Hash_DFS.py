# https://leetcode-cn.com/problems/kill-process/
# Hash + DFS

class Solution:
    def killProcess(self, pid, ppid, kill):
        n = len(pid)
        # Hash
        mpppid = {}
        for i in range(n):
            if ppid[i] in mpppid.keys():
                mpppid[ppid[i]].append(i)
            else:
                mpppid[ppid[i]] = [i]
        # mpppid存了ppid[i]的location，用location去找对应的子pid
        # print(mpppid)
        res = [kill]

        def dfs(x):
            if not x in mpppid.keys():
                return
            for i in mpppid[x]:
                # print(i, pid[i])
                y = pid[i]
                res.append(y)
                dfs(y)

        dfs(kill)
        return res


pid =  [1, 3, 10, 5]
ppid = [3, 0, 5, 3]
kill = 5
print(Solution().killProcess(pid, ppid, kill))
