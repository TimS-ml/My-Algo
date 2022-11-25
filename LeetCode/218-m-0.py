'''
goal: calc space, no overlap

case:
- start [1, 3, 5] [2, 3, 6]
- end   [1, 3, 5] [2, 3, 6]
    - sort desc

- sweep line
- event [1, 5] [3, 0] | [2, 6] [3, 0]
- maintain (sweep line) sth for end checking
    - heap
'''

from heapq import heappush, heappop

class Solution:
    # heap
    def getSkyline(self, buildings):
        events = []
        for b in buildings:
            # trigger, hight, buffer(end)
            events.append([b[0], b[2], b[1]])
            events.append([b[1], 0, None])
        
        events = sorted(events, key=lambda x: (x[0], -x[1]))

        # sweep
        ans = [(0, 0)]  # buffer
        currB = [(0, float('inf'))]  # currBuilding for end check

        '''
        case: [[15,20,10],[19,24,8]]
        at [19, 24]:
        currB: [both building 10 and 8]
        '''
        for trig, hight, buffer in events:
            # start of some b
            if hight > 0:
                # if hight > ans[-1][1]:
                #     ans.append([trig, hight])
                heappush(currB, (-hight, buffer))
            
            # update currB
            while currB[0][1] <= trig:
                heappop(currB)
            
            # end of some b
            # if hight == 0:
            #     # print(currB, ans)

            # only check the height changes instead of start and end
            if -currB[0][0] != ans[-1][1]:
                ans.append([trig, -currB[0][0]])

        return ans[1:]

    # bf
    def getSkyline_bf(self, buildings):
        events = []
        for b in buildings:
            # trigger, hight, buffer(end)
            events.append([b[0], b[2], b[1]])
            events.append([b[1], 0, None])
        
        events = sorted(events, key=lambda x: (x[0], -x[1]))

        # sweep
        ans = [(-1, -1)]  # buffer
        currB = [(float('inf'), 0)]  # currBuilding for end check
        for trig, hight, buffer in events:
            # start of some b
            if hight > 0:
                if hight > ans[-1][1]:
                    ans.append([trig, hight])
                currB.append([buffer, hight])

            # update currB
            currB = filter(lambda x: x[0] > trig, currB)
            currB = sorted(currB, key=lambda x: -x[1])
            
            # print(trig, hight, currB)
            
            # end of some b
            if hight == 0:
                print(currB, ans)
                if currB[0][1] != ans[-1][1]:
                    ans.append([trig, currB[0][1]])

        return ans[1:]
