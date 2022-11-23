'''
# Code Explain:
- Time complexity: O(NlogN)
- Space complexity: O(N)

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
    endHeap: (-height, end)  -> max heap by height
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

        # 保存返回结果
        ans = [[0, 0]]

        # 最小堆, 保存当前最高的轮廓(-H, R), 用-H转换为最大堆, R的作用是记录该轮廓的有效长度
        endHeap = [(0, float("inf"))]

        # 从左至右遍历关键事件
        for L, negH, R in events:

            # 如果是轮廓升高事件, 记录到最小堆中
            if negH: heappush(endHeap, (negH, R))

            # 获取当前最高轮廓
            # 根据当前遍历的位置L, 判断最高轮廓是否有效
            # 如果无效则剔除, 让次高的轮廓浮到堆顶, 继续判断
            while endHeap[0][1] <= L:
                heappop(endHeap)

            # 如果当前的最高轮廓发生了变化, 则记录一个关键点
            if ans[-1][1] != -endHeap[0][0]:
                ans += [ [L, -endHeap[0][0]] ]
        return ans[1:]


    # offical solution
    # using only one (height, end position) heap
    def getSkyline_3(self, buildings: List[List[int]]) -> List[List[int]]:
        # Iterate over all buildings, for each building i,
        # add (position, i) to edges.
        edges = []
        for i, build in enumerate(buildings):
            edges.append([build[0], i])
            edges.append([build[1], i])

        # Sort edges by non-decreasing order.
        edges.sort()

        # Initailize an empty Priority Queue 'endHeap' to store all the
        # newly added buildings, an empty list answer to store the skyline key points.
        endHeap, ans = [], []
        idx = 0

        # Iterate over all the sorted edges.
        while idx < len(edges):

            # Since we might have multiple edges at same x,
            # Let the 'curr_x' be the current position.
            curr_x = edges[idx][0]

            # While we are handling the edges at 'curr_x':
            while idx < len(edges) and edges[idx][0] == curr_x:
                # The index 'b' of this building in 'buildings'
                b = edges[idx][1]

                # If this is a left edge of building 'b', we
                # add (height, right) of building 'b' to 'endHeap'.
                if buildings[b][0] == curr_x:
                    right = buildings[b][1]
                    height = buildings[b][2]
                    heappush(endHeap, [-height, right])

                # If the tallest endHeap building has been passed,
                # we remove it from 'endHeap'.
                while endHeap and endHeap[0][1] <= curr_x:
                    heappop(endHeap)
                idx += 1

            # Get the maximum height from 'endHeap'.
            max_height = -endHeap[0][0] if endHeap else 0

            # If the height changes at this curr_x, we add this
            # skyline key point [curr_x, max_height] to 'answer'.
            if not ans or max_height != ans[-1][1]:
                ans.append([curr_x, max_height])

        # Return 'answer' as the skyline.
        return ans
