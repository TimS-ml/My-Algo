# https://leetcode-cn.com/problems/queue-reconstruction-by-height/


class Solution:
    def reconstructQueue(self, people):
        queue = []
        for p in sorted(people, key=lambda x: (x[0],x[1] and -x[1]), reverse=True):
        # for p in sorted(people, key=lambda (h,k): (-h,k)):  # don't work
            queue.insert(p[1], p)
        return queue


people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
print(Solution().reconstructQueue(people))
