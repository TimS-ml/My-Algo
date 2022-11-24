'''
# Code Explain:
- Time complexity: O(N ** 2)
- Space complexity: O(N)

If a building with height h covers the indexes from x_i to x_j, then all the indexes from x_i to x_j (exclusive) have the height of h at least. Notice that the right edge of a building doesn't count!

Brute force 1:
- iter
- we update the maximum height for **all** the indexes within the range [left_index, right_index)
- traverse the updated heights and output all the positions where height changes as skyline key points!

Brute force 2 - sweep line:
- Initialize an empty list answer for skyline key points.
- Use a set (edgeSet) to store all distinct edges in buildings.
- Iterate over the sorted positions, and for each position:
- Check for buildings that **intersect** with the imaginary vertical line at position. (A building is considered to be intersecting with the line if position is within the range [left, right).)
- The max_height is the maximum height of the intersecting buildings at position, or 0 if no building intersects with the line.
- If max_height differs from that of the previous skyline point, add a new skyline point to answer.
- Return answer as the skyline.
'''

from typing import List

# brute force
class Solution:
    # leads to union find
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # Sort the unique positions of all the edges.
        # for building in buildings -> for x in building[:2] -> x
        positions = sorted(list(set([x for building in buildings for x in building[:2]])))

        # Hast table 'edge_index_map' to record every {position : index} pairs in edges.
        edge_index_map = {x : i for i, x in enumerate(positions)}

        # Initialize 'heights' to record maximum height at each index.
        heights = [0] * len(positions)

        # Iterate over all the buildings.
        for left, right, height in buildings:
            # For each building, find the indexes of its left
            # and right edges.
            left_idx = edge_index_map[left]
            right_idx = edge_index_map[right]

            # Update the maximum height within the range [left_idx, right_idx)
            for i in range(left_idx, right_idx):
                heights[i] = max(heights[i], height)

        answer = []

        # Iterate over 'heights'.
        for i in range(len(heights)):
            curr_height = heights[i]
            curr_x = positions[i]

            # Add all the positions where the height changes to 'answer'.
            if not answer or answer[-1][1] != curr_height:
                answer.append([curr_x, curr_height])
        return answer

    # leads to heap
    def getSkyline_2(self, buildings: List[List[int]]) -> List[List[int]]:
        # Collect and sort the unique positions of all the edges.
        # for building in buildings -> for x in building[:2] -> x
        positions = sorted(list(set([x for building in buildings for x in building[:2]])))

        # 'answer' for skyline key points
        answer = []

        # For each position, draw an imaginary vertical line.
        for position in positions:
            # current max height.
            max_height = 0

            # Iterate over all the buildings:
            for left, right, height in buildings:
                # Update 'max_height' if necessary.
                if left <= position < right:
                    max_height = max(max_height, height)

            # If its the first key point or the height changes,
            # we add [position, max_height] to 'answer'.
            if not answer or max_height != answer[-1][1]:
                answer.append([position, max_height])

        # Return 'answer' as the skyline.
        return answer

