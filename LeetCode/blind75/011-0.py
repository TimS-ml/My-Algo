'''
two pointers l and r
update max(water)
[1,8,6,2,5,4,8,3,7]
 l               r
greedy

case: [1,2,4]
case: [1,3,2,5,25,24,5]

wrong sol vs correct sol:

w: min(h[l+1], h[r]) > min(h[l], h[r-1])
c: h[l] <= h[r]

当有两种选择，left 右移动 or right 左移动，当h[left]<h[right] 当right左移
        1.if h[right-1]>=h[right]: 由于h[left]矮，container高度还是h[left]，而宽度却少了1，这样只会造成area减少，不可取抛弃；
        2.if h[right-1]<h[right]: container高度减小，宽度减少1，area减少，不可取抛弃；
        综上，**如果走高的一方，只会使得container整体area朝减少的方向走，不可取**
所以，正确做法是每次走矮的一方，才有可能朝area增大的方向走；

also, another way of understanding (like DP)
https://leetcode.com/problems/container-with-most-water/discuss/6099/Yet-another-way-to-see-what-happens-in-the-O(n)-algorithm
'''

from typing import List

class Solution:
    # wrong
    def maxArea_w(self, h: List[int]) -> int:
        def getCap(l, r):
            return (r - l) * min(h[l], h[r])

        l, r = 0, len(h) - 1
        maxcap = 0
        while l < r:  # ends at l >= r
            cap = getCap(l, r)
            maxcap = max(maxcap, cap)
            if getCap(l+1, r) > getCap(l, r-1):
                l += 1
            else:
                r -= 1
        return maxcap

    def maxArea(self, h: List[int]) -> int:
        maxcap = 0
        l, r = 0, len(h) - 1
        
        while l < r:
            width = r - l
            maxcap = max(maxcap, min(h[l], h[r]) * width)
            if h[l] <= h[r]:
                l += 1
            else:
                r -= 1
                
        return maxcap
