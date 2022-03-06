'''
# Code Explain:
- Time complexity: O(n)
- Space complexity: O(n)

Solution
random pick one element from list
case: [1, 2, 3, 4]
- calc ratio: [0.1, 0.2, 0.3, 0.4]

- by generating a large seqence
    - seq = [0, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    - random pick one, return number (index)

- genrate a random number between 0 and 1
    - figure out the range this random number in

This solution could be optimized, check sol1 in 528-0.py
- cumsum could be replaced by a for loop
- no need to do element/sum, simply random * sum
- prefix sums + binary search is a better solution
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
