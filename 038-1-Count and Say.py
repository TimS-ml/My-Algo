# https://leetcode-cn.com/problems/count-and-say/


class Solution:
    def countAndSay(self, n) -> str:
        ans = "1"
        n -= 1
        while n > 0:
            temp = ""
            curr = ans[0]
            count = 1
            for i in range(1, len(ans)):
                if curr == ans[i]:
                    count += 1
                else:
                    temp += str(count) + curr
                    curr = ans[i]
                    count = 1
            temp += str(count) + curr
            ans = temp
            n -= 1
        return ans


print(Solution().countAndSay(5))
