'''
# Code Explain:
- Time complexity: O(N logK)
It's O(N log2K) slower than quick sort
- Space complexity: O(K)

# Thought process
[1] sort the list
  - easy way: nums.sort(reverse=True), time: O(N * log(N))
  - heapq in python: O(N * log(2N))
    - in python, heappop will pop minimum value
  - Merge Sort or Quick Sort: O(N * log(N))
[2] located the kth number
  - k start at 1

# Test cases
3,2,3,1,2,4,5,5,6
4

'''

from typing import List
import random
# from heapq import heapify, heappop, heappush


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(left, right, pivot_index):
            pivot = nums[pivot_index]
            # 1. move pivot to end
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]  
            
            # 2. move all smaller elements to the left
            store_index = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[store_index], nums[i] = nums[i], nums[store_index]
                    store_index += 1

            # 3. move pivot to its final place
            nums[right], nums[store_index] = nums[store_index], nums[right]  
            
            return store_index
        
        def select(left, right, k_smallest):
            """
            Returns the k-th smallest element of list within left..right
            """
            if left == right:       # If the list contains only one element,
                return nums[left]   # return that element
            
            # select a random pivot_index between 
            pivot_index = random.randint(left, right)     
                            
            # find the pivot position in a sorted list   
            pivot_index = partition(left, right, pivot_index)
            
            # the pivot is in its final sorted position
            if k_smallest == pivot_index:
                 return nums[k_smallest]
            # go left
            elif k_smallest < pivot_index:
                return select(left, pivot_index - 1, k_smallest)
            # go right
            else:
                return select(pivot_index + 1, right, k_smallest)

        # kth largest is (n - k)th smallest 
        return select(0, len(nums) - 1, len(nums) - k)


nums1 = [3, 2, 3, 1, 2, 4, 5, 5, 6]  # 4
k1 = 4

nums2 = [3, 2, 1, 5, 6, 4]  # 5
k2 = 2
print(Solution().findKthLargest(nums1, k1))
print(Solution().findKthLargest(nums2, k2))
