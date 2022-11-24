'''
# Code Explain:
- Time complexity: O(NlogN)
- Space complexity: O(N)

'''

class Solution(object):
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
        idx = 0
        
        # Iterate over all the sorted edges.
        while idx < len(edges):
            # Since we might have multiple edges at same x,
            # Let the 'curr_x' be the current position.
            curr_x = edges[idx][0]
            
            # While we are handling the edges at 'curr_x':
            while idx < len(edges) and edges[idx][0] == curr_x:
                height = edges[idx][1]
                
                # If 'height' > 0, meaning a building of height 'height'
                # is live, push 'height' to 'live'. 
                # Otherwise, a building of height 'height' is passed, 
                # push the height to 'past'.
                if height > 0:
                    heapq.heappush(live, -height)
                else:
                    heapq.heappush(past, height)
                idx += 1
            
            # While the top height from 'live' equals to that from 'past',
            # Remove top height from both 'live' and 'past'.
            while past and past[0] == live[0]:
                heapq.heappop(live)
                heapq.heappop(past)
            
            # Get the maximum height from 'live'.
            max_height = -live[0] if live else 0
            
            # If the height changes at 'curr_x', we add this
            # skyline key point [curr_x, max_height] to 'answer'.
            if not answer or answer[-1][1] != max_height:
                answer.append([curr_x, max_height])
                
        # Return 'answer' as the skyline.
        return answer            
