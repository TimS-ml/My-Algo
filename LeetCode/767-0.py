'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''

import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, S: str) -> str:
        pq = [(-S.count(x), x) for x in set(S)]
        # print(pq)
        heapq.heapify(pq)
        if any(-nc > (len(S) + 1) / 2 for nc, x in pq):
            return ''

        ans = []
        while len(pq) >= 2:
            nct1, ch1 = heapq.heappop(pq)
            nct2, ch2 = heapq.heappop(pq)
            # This code turns out to be superfluous, but explains what is happening
            # if not ans or ch1 != ans[-1]:
            #     ans.extend([ch1, ch2])
            # else:
            #     ans.extend([ch2, ch1])
            ans.extend([ch1, ch2])
            if nct1 + 1:
                heapq.heappush(pq, (nct1 + 1, ch1))
            if nct2 + 1:
                heapq.heappush(pq, (nct2 + 1, ch2))
        return ''.join(ans) + (pq[0][1] if pq else '')


    def reorganizeString_2(self, S):
        ans = []
        pq = [(-value,key) for key,value in Counter(S).items()]
        heapq.heapify(pq)
        p_a, p_b = 0, ''
        while pq:
            a, b = heapq.heappop(pq)
            ans += [b]
            if p_a < 0:
                heapq.heappush(pq, (p_a, p_b))
            a += 1
            p_a, p_b = a, b
        ans = ''.join(ans)
        # a smart way to check
        if len(ans) != len(S): 
            return ''
        return ans
