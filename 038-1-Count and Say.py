# https://leetcode-cn.com/problems/count-and-say/


class Solution:
    def countAndSay(self, n) -> str:
        ans = "1"
        n -= 1
        while n > 0:
            res = ""  # 存储生成的答案
            pre = ans[0]  # 111输出：3个1里面的“1”
            count = 1  # 111输出：3个1里面的“3”
            for i in range(1, len(ans)):
                if pre == ans[i]:
                    count += 1
                else:
                    res += str(count) + pre
                    pre = ans[i]
                    count = 1
            res += str(count) + pre
            ans = res  # ans是当前n的输出，同时也是下一个n的输入
            n -= 1
        return ans


print(Solution().countAndSay(5))
