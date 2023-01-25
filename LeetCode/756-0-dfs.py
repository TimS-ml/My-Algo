'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''

from collections import defaultdict
from itertools import product


class Solution(object):
    # If the first two characters appears in the blockDict, append the top element to nextLayer variable and call DFS. 
    # If we reach the last two characters in bottomLayer, we set nextLayer to bottomLayer, set empty to nextLayer, and call DFS.
    def pyramidTransition(self, bottom, allowed):
        if len(bottom) <= 1:
            return False

        # init a dict of List
        # bottom - top mapping
        blockDict = {}
        for block in allowed:
            if block[:2] not in blockDict:
                blockDict[block[:2]] = []

            blockDict[block[:2]].append(block[2])

        def dfs(bottomLayer, nextLayer):
            print(bottomLayer, nextLayer)

            if len(bottomLayer) == 1:
                return True

            if bottomLayer[:2] in blockDict:
                # only pair the first 2 chars!!!
                for nextElement in blockDict[bottomLayer[:2]]:
                    if len(bottomLayer) <= 2:
                        # move to next layer (move nextLayer to bottomLayer)
                        if dfs(nextLayer + nextElement, ""):
                            return True
                    else:
                        if len(nextLayer) <= 0 or \
                            (nextLayer[-1] + nextElement) in blockDict:
                            # move to next char
                            if dfs(bottomLayer[1:], nextLayer + nextElement):
                                return True

            return False

        return dfs(bottom, "")


    # TLE
    def pyramidTransition_2(self, bottom, allowed):
        f = defaultdict(lambda: defaultdict(list))
        for a, b, c in allowed:
            f[a][b].append(c)

        def pyramid(bottom):
            if len(bottom) == 1: return True
            for i in product(*(f[a][b] for a, b in zip(bottom, bottom[1:]))):
                if pyramid(i): return True
            return False

        return pyramid(bottom)


bottom = "BCD"
allowed = ["BCC","CDE","CEA","FFF"]
print(Solution().pyramidTransition(bottom, allowed))

