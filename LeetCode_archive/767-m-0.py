'''
[0] 
[1] freq dict
    heap, max heap (-freq, char)

case 1
aabbccdd

pop
    currChar = a
pop again
    currChar = b
    put a back


case 2
aaab
currchar not None, freq > 1 and heap = []
    ???
'''

from collections import Counter
from heapq import heappush, heappop

class Solution:
    def reorganizeString(self, s: str) -> str:
        dic = Counter(list(s))
        print(dic)
        maxH = []
        for k, v in dic.items():
            heappush(maxH, [-v, k])
        # print(maxH[0])
        
        prevF, prev = heappop(maxH)
        ans = [prev]
        
        while maxH:
            currF, curr = heappop(maxH)
            ans.append(curr)
            
            if prevF + 1 < 0:
                heappush(maxH, [prevF + 1, prev])
            
            # print(currF, curr, prevF + 1, prev, ans)
            prevF, prev = currF, curr
        
        
        # print(prevF, prev, ans)
        # [aba], preF = -2
        if prevF + 1 != 0:
            return ''
        else:
            # ans.append(prev)
            return ''.join(ans)

