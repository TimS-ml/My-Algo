# Links
https://leetcode.com/problems/shortest-path-in-binary-matrix/

# Thought Process
https://leetcode.com/problems/shortest-path-in-binary-matrix/discuss/313347/A*-search-in-Python
An `A*` search is like a breadth-first seach, except that in each iteration, instead of expanding the cell with the shortest path from the origin, we expand the cell with the lowest overall estimated path length -- this is the distance so far, plus a heuristic (rule-of-thumb) estimate of the remaining distance. As long as the heuristic is consistent, an A* graph-search will find the shortest path. This can be somewhat more efficient than breadth-first-search as we typically don't have to visit nearly as many cells. Intuitively, an A* search has an approximate sense of direction, and uses this sense to guide it towards the target.

# Test Cases

