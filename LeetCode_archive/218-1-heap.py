'''
# Code Explain:
- Time complexity: O(NlogN)
- Space complexity: O(N)

intervals intersection
we don't care the connection in [start, end], we only care about max number of overlap
similar to 253, so we can break start and end
'''

from typing import List
from heapq import heappush, heappop


class Solution:
    '''
    track all positions (start and end)
    endHeap: (-height, end)  -> max heap by height
    pop rules: index, when current is ahead of end position
    for each position
        - update heap by idx
        - when left <= current position
    '''
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        # `position` stores all coordinates where the largest height may change
        # `endHeap` stores all buildings whose ranges cover the current coordinate
        position = sorted(set([building[0] for building in buildings] + [building[1] for building in buildings]))
        idx, prevH = 0, 0
        endHeap, ans = [], []

        for curPos in position:
            # pop buildings that end at or before `curPos` out of the priority queue
            # they are no longer "endHeap"
            while endHeap and endHeap[0][1] <= curPos:
                heappop(endHeap)

            # push [negative_height, end_point] of all buildings onto the priority queue that:
            # - start before `curPos`
            # they are candidates for the current highest building
            while idx < len(buildings) and buildings[idx][0] <= curPos:
                heappush(endHeap, [-buildings[idx][2], buildings[idx][1]])
                idx += 1

            # now endHeap[0] must be the largest height at the current position
            if endHeap:
                curH = -endHeap[0][0]
                if curH != prevH:
                    ans.append([curPos, curH])
                    prevH = curH
            else:  # no building -> horizon
                ans.append([curPos, 0])

        return ans


    '''
    track all positions (start and end)
        - this solution pack infos together: start (trigger and sorted), height, end
        - (R, 0, 0)
    endHeap: (-height, end)  -> max heap by height
        - only push height !=0
    pop rules: index, when current is ahead of end position
    for each position
        - update heap by idx
        - when left <= current position
    '''
    def getSkyline_2(self, buildings):
        # 不难发现这些关键点的特征是: 竖直线上轮廓升高或者降低的终点
        # 所以核心思路是: 从左至右遍历建筑物, 记录当前的最高轮廓, 如果产生变化则记录一个关键点

        # 首先记录构造一个建筑物的两种关键事件
        # 第一种是轮廓升高事件(L, -H), 第二种是轮廓降低事件(R, 0)
        # note: 轮廓升高事件(L, -H, R)中的R用于后面的最小堆
        events = [(L, -H, R) for L, R, H in buildings]
        events += list({(R, 0, 0) for _, R, _ in buildings})

        # 先根据L从小到大排序, 再根据H从大到小排序(记录为-H的原因)
        # 这是因为我们要维护一个堆保存当前最高的轮廓
        events.sort()

        # init place holder, remember to return ans[1:]
        ans = [[0, 0]]

        # yet another place holder, so we can skip check the heap
        endHeap = [(0, float("inf"))]

        # so for R,0,0:
        #   not trigger heap push
        #   trigger heap pop
        #   trigger ans update
        for L, negH, R in events:

            # 如果是轮廓升高事件, 记录到最小堆中
            if negH != 0:
                heappush(endHeap, (negH, R))

            # pop buildings that end at or before `L` out of the priority queue
            while endHeap[0][1] <= L:
                heappop(endHeap)

            # 如果当前的最高轮廓发生了变化, 则记录一个关键点
            if ans[-1][1] != -endHeap[0][0]:
                ans += [ [L, -endHeap[0][0]] ]
        return ans[1:]


    # offical solution, similar to sol2, but worse more if else check since it's not bind end position to start during looping
    # using only one (height, end position) heap
    def getSkyline_3(self, buildings: List[List[int]]) -> List[List[int]]:
        # Iterate over all buildings, for each building i,
        # add (position, building idx) to edges.
        edges = []
        for buildingIdx, build in enumerate(buildings):
            edges.append([build[0], buildingIdx])
            edges.append([build[1], buildingIdx])
        edges.sort()

        # Initailize an empty Priority Queue 'endHeap' to store all the
        # newly added buildings, an empty list answer to store the skyline key points.
        endHeap, ans = [], []
        edgeIdx = 0

        # Iterate over all the sorted edges.
        while edgeIdx < len(edges):

            # Since we might have multiple edges at same x,
            # Let the 'curPos' be the current position.
            curPos = edges[edgeIdx][0]

            # While we are handling the edges at 'curPos':
            while edgeIdx < len(edges) and edges[edgeIdx][0] == curPos:
                buildingIdx = edges[edgeIdx][1]

                # If this is a left edge of building 'b', we
                # add (height, right) of building 'b' to 'endHeap'.
                # !!! case: edges is end of building
                #     then buildings[buildingIdx] != curPos
                # so only update heap when start of the building, but inside heap it's height and end of the building
                if buildings[buildingIdx][0] == curPos:
                    right = buildings[buildingIdx][1]
                    height = buildings[buildingIdx][2]
                    heappush(endHeap, [-height, right])

                # If the tallest endHeap building has been passed,
                # we remove it from 'endHeap'.
                while endHeap and endHeap[0][1] <= curPos:
                    heappop(endHeap)
                edgeIdx += 1

            # Get the maximum height from 'endHeap'.
            max_height = -endHeap[0][0] if endHeap else 0

            # If the height changes at this curPos, we add this
            # skyline key point [curPos, max_height] to 'answer'.
            if not ans or max_height != ans[-1][1]:
                ans.append([curPos, max_height])

        # Return 'answer' as the skyline.
        return ans


class Solution_2(object):
    # two heap solution
    '''
    so we still need to mark l r info in edges
    replace sorted start point with a heap
    two heap patten is to find mid point, pop from one min heap and insert to another max heap
    but it's still double sort pattern
    '''
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # Iterate over the left and right edges of all the buildings, 
        # If its a left edge, add (left, height) to 'edges'.
        # Otherwise, add (right, -height) to 'edges'.
        edges = []
        for left, right, height in buildings:
            edges.append([left, height])
            edges.append([right, -height])
        edges.sort()
        
        # Initailize two empty priority queues 'live' and 'past' 
        # for the live buildings and the past buildings.
        live, past = [], []
        answer = []
        edgeIdx = 0
        
        # Iterate over all the sorted edges.
        while edgeIdx < len(edges):
            # Since we might have multiple edges at same x,
            # Let the 'curPos' be the current position.
            curPos = edges[edgeIdx][0]
            
            # While we are handling the edges at 'curPos':
            while edgeIdx < len(edges) and edges[edgeIdx][0] == curPos:
                height = edges[edgeIdx][1]
                
                # If 'height' > 0, meaning a building of height 'height'
                # is live, push 'height' to 'live'. 
                # Otherwise, a building of height 'height' is passed, 
                # push the height to 'past'.
                if height > 0:
                    heappush(live, -height)
                else:
                    heappush(past, height)
                edgeIdx += 1
            
            # While the top height from 'live' equals to that from 'past',
            # Remove top height from both 'live' and 'past'.
            while past and past[0] == live[0]:
                heappop(live)
                heappop(past)
            
            # Get the maximum height from 'live'.
            max_height = -live[0] if live else 0
            
            # If the height changes at 'curPos', we add this
            # skyline key point [curPos, max_height] to 'answer'.
            if not answer or answer[-1][1] != max_height:
                answer.append([curPos, max_height])
                
        # Return 'answer' as the skyline.
        return answer            
