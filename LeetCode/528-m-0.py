'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

Solution 1
random pick one element from list
case 1: [1, 3]
- calc ratio: [0.25, 0.75]
- seq = [0, 1, 1, 1]
- random pick one


Solution 2
Genrate a random number between 0 and 1
Figure out the rang this random number is in
'''

from typing import List
import itertools, random

class Solution:
    def __init__(self, w: List[int]):
        s = sum(w)
        self.probList = [i/s for i in w]
        self.probList = list(itertools.accumulate(self.probList))
        self.probList.insert(0, 0)
        
    def pickIndex(self) -> int:
        prob = random.uniform(0, 1)
        for i in range(len(self.probList) - 1):
            if self.probList[i] <= prob < self.probList[i+1]:
                return i


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
