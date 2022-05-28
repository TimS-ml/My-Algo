'''
# Code Explain:
- Time complexity: O(N logK)
- Space complexity: O(K)

# Thought process
[1] sort the list
  - easy way: nums.sort(reverse=True), time: O(N * log(N))
  - heapq in python: O(N * log(2N))
    - in python, heappop will pop minimum value
  - Merge Sort or Quick Sort: O(N * log(N))
[2] located the kth number
  - k start at 1
'''

from typing import List
import random


class Solution:
    # Let's implement a quick sort, then return nums[-k]
    def findKthLargest_2(self, nums: List[int], k: int) -> int:
        def partition(start, end, nums):
            # Initializing pivot's index to start
            pivot_index = start
            pivot = nums[pivot_index]
             
            # This loop runs till start pointer crosses
            # end pointer, and when it does we swap the
            # pivot with element on end pointer
            while start < end:
                 
                # Increment the start pointer till it finds an
                # element greater than  pivot
                while start < len(nums) and nums[start] <= pivot:
                    start += 1
                     
                # Decrement the end pointer till it finds an
                # element less than pivot
                while nums[end] > pivot:
                    end -= 1
                 
                # If start and end have not crossed each other,
                # swap the numbers on start and end
                if start < end:
                    nums[start], nums[end] = nums[end], nums[start]
             
            # Swap pivot element with element on end pointer.
            # This puts pivot on its correct sorted place.
            nums[end], nums[pivot_index] = nums[pivot_index], nums[end]
            
            # Returning end pointer to divide the nums into 2
            return end
             
        # The main function that implements QuickSort
        # no return needed, sort in place
        def quick_sort(start, end, nums):
            if start < end:
                # p is partitioning index, nums[p]
                # is at end place
                p = partition(start, end, nums)
                 
                # Sort elements before partition
                # and after partition
                quick_sort(start, p - 1, nums)
                quick_sort(p + 1, end, nums)
        
        quick_sort(0, len(nums)-1, nums)
        print(nums)
        return nums[-k]


    def findKthLargest(self, nums: List[int], k: int) -> int:
        # rand as pivot
        def partition(start, end, nums):
            # Initializing pivot's index to [[random]]
            pivot_index = random.randint(start, end)
            
            pivot = nums[pivot_index]
            # !!! move pivot to start
            nums[pivot_index], nums[start] = nums[start], nums[pivot_index]
            
            store_index = start
            # This loop runs till start pointer crosses
            # end pointer, and when it does we swap the
            # pivot with element on end pointer
            while start < end:
                 
                # Increment the start pointer till it finds an
                # element greater than  pivot
                while start < len(nums) and nums[start] <= pivot:
                    start += 1
                     
                # Decrement the end pointer till it finds an
                # element less than pivot
                while nums[end] > pivot:
                    end -= 1
                 
                # If start and end have not crossed each other,
                # swap the numbers on start and end
                if(start < end):
                    nums[start], nums[end] = nums[end], nums[start]
             
            # Swap pivot element with element on end pointer.
            # This puts pivot on its correct sorted place.
            # !!! the end after while loop != the end before while loop
            nums[end], nums[store_index] = nums[store_index], nums[end]
            
            # Returning end pointer to divide the nums into 2
            return end

        # start as pivot
        # def partition_normal(start, end, nums):
        #     # Initializing pivot's index to start
        #     pivot_index = start

        #     pivot = nums[pivot_index]

        #     # This loop runs till start pointer crosses
        #     # end pointer, and when it does we swap the
        #     # pivot with element on end pointer
        #     while start < end:

        #         # Increment the start pointer till it finds an
        #         # element greater than  pivot
        #         while start < len(nums) and nums[start] <= pivot:
        #             start += 1

        #         # Decrement the end pointer till it finds an
        #         # element less than pivot
        #         while nums[end] > pivot:
        #             end -= 1

        #         # If start and end have not crossed each other,
        #         # swap the numbers on start and end
        #         if(start < end):
        #             nums[start], nums[end] = nums[end], nums[start]

        #     # Swap pivot element with element on end pointer.
        #     # This puts pivot on its correct sorted place.
        #     nums[end], nums[pivot_index] = nums[pivot_index], nums[end]

        #     # Returning end pointer to divide the nums into 2
        #     return end
        
        def select(start, end, nums, k_smallest):
            """
            Returns the k-th smallest element of list within left..right
            In this modify quick sort, you only need to sort the number <= pivot
            And you need to return something
            """
            if start == end:  # only one number
                return nums[start]

            if start < end:
                # p is partitioning index, nums[p]
                # is at end place
                p = partition(start, end, nums)
                
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
# print(Solution().findKthLargest_2(nums1, k1))
# print(Solution().findKthLargest_2(nums2, k2))
