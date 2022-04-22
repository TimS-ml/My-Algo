'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

case:

            |--2--|
      |--1--|     |--1--|
|--0--|                 |--0--|
It's hard to calculate '0' and '1' by deduct overlaps
'''

class Solution:
    def exclusiveTime(self, n, logs):
        ans, stack = [0] * n, []
        for log in logs:
            f_id, event, time = log.split(':')
            f_id, time = int(f_id), int(time)
            if event == 'start':
                # end previous f_id and update time
                if stack:
                    ans[stack[-1][0]] += time - stack[-1][1]
                stack.append([f_id, time])
            else:
                top = stack.pop()
                ans[top[0]] += time - top[1] + 1
                if stack:
                    stack[-1][1] = time + 1
        return ans

    def exclusiveTime_2(self, n, logs):
        ans, stack = [0] * n, []
        for log in logs:
            f_id, event, time = log.split(':')
            f_id, time = int(f_id), int(time)
            if event == 'start':
                stack.append([f_id, time])
            else:
                top = stack.pop()
                ans[top[0]] += time - top[1] + 1
                if stack:
                    # note: here stack is after poped
                    ans[stack[-1][0]] -= time - top[1] + 1
        return ans
