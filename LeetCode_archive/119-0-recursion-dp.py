'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''


class Solution(object):
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]
        li1 = self.getRow(rowIndex - 1)
        li2 = [0] + li1[:-1]
        ans = [a + b for a, b in zip(li1, li2)]
        ans.append(li1[-1])
        return ans

    def getRow_2(self, rowIndex):
        ans = [1] * (rowIndex + 1)
        for i in range(2, rowIndex + 1):
            for j in range(i - 1, 0, -1):
                ans[j] += ans[j - 1]
        return ans

    def getRow_3(self, rowIndex):
        ans = [1]
        for i in range(rowIndex):
            ans = [sum(x) for x in zip(ans + [0], [0] + ans)]
        return ans

print(Solution().getRow(5))
