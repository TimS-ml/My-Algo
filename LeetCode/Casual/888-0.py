'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()



Swap a[i] and b[j] so that sum(a)==sum(b)

case: aliceSizes = [1,2], bobSizes = [2,3]
[1] raw_sum_a - raw_sum_b => -2
[2] find a[i]-b[j] == (raw_sum_a-raw_sum_b)/2 (this is a int)
- brute force
- hash list a

if not:
1 <= aliceSizes.length <= 10000
1 <= bobSizes.length <= 10000
special case: aliceSizes = [], bobSizes = [2,2]
'''

from typing import List


class Solution:
    def fairCandySwap_brute(self, aliceSizes: List[int],
                            bobSizes: List[int]) -> List[int]:
        target = int((sum(aliceSizes) - sum(bobSizes)) / 2)
        for i in range(len(aliceSizes)):
            for j in range(len(bobSizes)):
                if aliceSizes[i] - bobSizes[j] == target:
                    return [aliceSizes[i], bobSizes[j]]

    def fairCandySwap(self, aliceSizes: List[int],
                      bobSizes: List[int]) -> List[int]:
        target = int((sum(aliceSizes) - sum(bobSizes)) / 2)
        alice_hash = set(aliceSizes)
        for j in range(len(bobSizes)):
            if target + bobSizes[j] in alice_hash:
                return [target + bobSizes[j], bobSizes[j]]


a = [1, 1]
b = [2, 2]
print(Solution().fairCandySwap(a, b))
