# https://leetcode-cn.com/problems/count-and-say/


class Solution:
    def countAndSay(self, n) -> str:
        s = '1' 
        if n == 1:
            return '1'
        for _ in range(n-1):
            curr = s[0] 
            count = 0
            ans = ''
            for i in range(len(s)):
                if s[i] == curr:
                    count += 1
                else:
                    ans = ans + str(count) + curr
                    curr = s[i]
                    count = 1
            ans = ans + str(count) + curr
            curr = s[i]
            count = 1
            s = ans
        return ans


n = 5
print(Solution().countAndSay(n))

