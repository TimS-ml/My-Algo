'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

For a group of continuous same characters,
we need to delete all the group but leave only one character.

cost = sum_cost(group) - max_cost(group)
'''

class Solution:
    def minCost(self, s, cost):
        ans = max_cost = 0
        for i in range(len(s)):
            if i > 0 and s[i] != s[i - 1]:
                max_cost = 0  # reset to 0
            # for multi same char, only keep one smallest value and append rest to ans
            ans += min(max_cost, cost[i])
            max_cost = max(max_cost, cost[i])
        return ans

    # two pointers
    def minCost_2(self, colors: str, neededTime: List[int]) -> int:
        # Initalize two pointers i, j.
        total_time = 0
        i, j = 0, 0
        
        while i < len(neededTime) and j < len(neededTime):
            curr_total = 0
            curr_max = 0
            
            # Find all the balloons having the same color as the 
            # balloon indexed at i, record the total removal time 
            # and the maximum removal time.
            while j < len(neededTime) and colors[i] == colors[j]:
                curr_total += neededTime[j]
                curr_max = max(curr_max, neededTime[j])
                j += 1
            
            # Once we reach the end of the current group, add the cost of 
            # this group to total_time, and reset two pointers.
            total_time += curr_total - curr_max
            i = j
        
        return total_time
