'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''

class Solution:
    def partition(self, s):
        ans = []
        def backtrack(start, tmp):
            if start >= len(s):
                ans.append(tmp)
                return
            for end in range(start + 1, len(s) + 1):
                subS = s[start:end]
                if subS == subS[::-1]:
                    # backtrack(end, tmp + [subS])

                    # or you can use a more backtracking way
                    tmp.append(subS)
                    backtrack(end, tmp)
                    tmp.pop()

        backtrack(0, [])
        return ans

    # top down
    def partition_2(self, s):
        # pal[len(s)][len(s)], false填充
        # 相当于创建了一个二维表, 满足的地方填上True
        pal = [[False for i in range(len(s))] for j in range(len(s))]
        ans = [[[]]] + [[] for _ in range(len(s))]

        for i in range(0, len(s)):
            for j in range(0, i + 1):
                # 先and再or, 所以加括号
                # j+1 > i-1对应相邻的, 如cbaabc里的aa
                # pal[j+1][i-1]对应间隔的, 如cbaabc里的c-c和b-b
                if (s[j] == s[i]) and ((j + 1 > i - 1) or pal[j + 1][i - 1]):
                    pal[j][i] = True
                    print(pal, j, i)
                    for res in ans[j]:
                        a = res + [s[j:i + 1]]
                        ans[i + 1].append(a)
                        print(ans)
        return ans[-1]  # 列表里的倒数第一个元素


s = 'aab'
print(Solution().partition(s))
