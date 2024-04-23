'''
# Code Explain:
- Time complexity: O(N logN)
- Space complexity: O(logN)

- exactly n people arrive in each city => sort top n person for city a
Greedy problems usually look like "Find minimum number of something to do something" or "Find maximum number of something to fit in some conditions", and typically propose an unsorted input.
The idea of greedy algorithm is to pick the locally optimal move at each step, that will lead to the globally optimal solution.

case:
[100, 1], [99, 1], [99, 5], [97, 4]
'''

class Solution:
    def twoCitySchedCost(self, costs):
        # or just use: costs.sort(key = lambda x : x[0] - x[1])
        diffs = []
        for c1, c2 in costs:
            diffs.append([c2 - c1, c1, c2])
        diffs.sort()

        ans = 0
        for i in range(len(diffs)):
            if i < len(diffs) // 2:
                ans += diffs[i][2]
            else:
                ans += diffs[i][1]
        return ans
