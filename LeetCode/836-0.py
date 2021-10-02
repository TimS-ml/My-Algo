'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

# Pros and Cons and Notation:

case 1:
rec1 = [0,0,2,2], rec2 = [1,1,3,3]
[2,2] > [1,1]

case 2:
rec1 = [5,15,8,18], rec2 = [0,3,7,9]

- The rectangle is projected onto the coordinate axis and becomes an interval
  - For two overlapping rectangles, their projections on the xx axis and yy axis also overlap each other

- Should we checking both x and y overlap?
 - yes: case 2 x_overlap=True, y_overlap=False
    - rec1 on top of rec2
'''


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x_overlap = not (rec1[2] <= rec2[0] or rec2[2] <= rec1[0])
        y_overlap = not (rec1[3] <= rec2[1] or rec2[3] <= rec1[1])
        return x_overlap and y_overlap
