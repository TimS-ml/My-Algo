# https://leetcode-cn.com/problems/reorganize-string/
# https://leetcode.com/problems/reorganize-string/solution/

import heapq


class Solution:
    def reorganizeString(self, S: str) -> str:
        pq = [(-S.count(x), x) for x in set(S)]
        # print(pq)
        heapq.heapify(pq)
        if any(-nc > (len(S) + 1) / 2 for nc, x in pq):
            return ""

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
        return "".join(ans) + (pq[0][1] if pq else '')


S1 = "aaab"
S2 = "aab"
S3 = "a"
print(Solution().reorganizeString(S2))
