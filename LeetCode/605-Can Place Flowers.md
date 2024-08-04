# Links
https://leetcode.com/problems/can-place-flowers/description/


# Thought Process
https://www.youtube.com/watch?v=ZGxqqjljpUI

Cannot planted adjacent = 1, 0, 1 
Start from index 1 and check if the current index is 0 and the previous and next index is 0. If so, we can plant a flower at the current index. ...0, 0, 0... -> ... 0, 1, 0...
We can also check if the first and last index is 0 and plant a flower at the first index.


# Test Cases
0, 0, 0 -> 2 flowers

