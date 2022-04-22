'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

https://leetcode.com/problems/expression-add-operators/discuss/572099/C%2B%2BJavaPython-Backtracking-and-Evaluate-on-the-fly-Clean-and-Concise
There is no priority since there are no parentheses ( and ) in our s string, so we can evaluate the expression on the fly to save time.
For operator * and /, we need number before and after
'''

class Solution:
    def addOperators(self, s: str, target: int) -> List[str]:
        def backtrack(idx, path, resultSoFar, prevNum):
            if idx == len(s):
                if resultSoFar == target:
                    ans.append(path)
                return

            for i in range(idx, len(s)):
                # Skip leading zero number such as '03'
                if i > idx and s[idx] == '0':
                    break
                num = int(s[idx:i + 1])

                # very start, we need to init for first few chars
                # pick it without adding any operator
                # case "123456", first pick would be 1, 12, 123, 1234 ...
                if idx == 0:
                    backtrack(i + 1, path + str(num), resultSoFar + num, num)
                else:
                    backtrack(i + 1, path + "+" + str(num), resultSoFar + num, num)
                    backtrack(i + 1, path + "-" + str(num), resultSoFar - num, -num)
                    backtrack(i + 1, path + "*" + str(num), resultSoFar - prevNum + prevNum * num, prevNum * num)  # case: 1+2*3*4

        ans = []
        backtrack(0, "", 0, 0)
        return ans
