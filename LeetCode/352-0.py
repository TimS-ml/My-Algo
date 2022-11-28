'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

Append interval to heap when addNum called
Merge intervals when getIntervals called
'''

import heapq


class SummaryRanges(object):
    def __init__(self):
        self.intervals = []
        self.seen = set()

    def addNum(self, val):
        if val not in self.seen:
            self.seen.add(val)
            heapq.heappush(self.intervals, [val, val])
    
    # after this, will get empty heap
    def getIntervals(self):
        tmp = []

        while self.intervals:
            cur = heapq.heappop(self.intervals)
            # two number connected
            # step0: heap = [[4, 5], [6, 6], [9, 9]]
            # step1: tmp[-1] [4, 5] (end + 1 = 6)
            #        cur     [6, 6] (start = 6)
            if tmp and cur[0] <= tmp[-1][1] + 1:
                tmp[-1][1] = max(tmp[-1][1], cur[1])  # merge
            else:
                tmp.append(cur)

        # remember to update self.intervals!!!
        self.intervals = tmp
        return self.intervals


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
