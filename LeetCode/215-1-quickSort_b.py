'''
# Code Explain:
- Time complexity: O(N logK)
It's O(N log2K) slower than quick sort
- Space complexity: O(K)

# Thought process
Let's implement a more scalable way to start quick sort using random pivot
'''

from typing import List
import random


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition_rand(start, end, arr):
            rand_p = random.randrange(start, end)
            arr[start], arr[rand_p] = arr[rand_p], arr[start]
            return partition(start, end, arr)

        def partition(start, end, arr):
            piv_idx = start
            pivot = arr[piv_idx]

            while start < end:
                while start < len(arr) and arr[start] <= pivot:
                    start += 1

                while arr[end] > pivot:
                    end -= 1

                if start < end:
                    arr[start], arr[end] = arr[end], arr[start]
            
            # after while loop, move pivot to the right position
            # remember to save pivot idx first
            arr[end], arr[piv_idx] = arr[piv_idx], arr[end]
            
            return end  # end is the correct piv idx now

        def select(start, end, arr, k_smallest):
            if start == end:  # only one number
                return arr[start]

            if start < end:
                # p is partitioning index, nums[p]
                # is at end place
                p = partition_rand(start, end, nums)
                
                if k_smallest == p:
                    return nums[p]
                elif k_smallest < p:
                    return select(start, p - 1, nums, k_smallest)
                else:
                    return select(p + 1, end, nums, k_smallest)

        # kth largest is (n - k)th smallest 
        ans = select(0, len(nums) - 1, nums, len(nums) - k)
        print(nums)
        return ans



# nums1 = [3]  # 4
# k1 = 1

nums1 = [3, 2, 3, 1, 2, 4, 5, 5, 6]  # 4
k1 = 4

nums2 = [3, 2, 1, 5, 6, 4]  # 5
k2 = 2

print(Solution().findKthLargest(nums1, k1))
print(Solution().findKthLargest(nums2, k2))
