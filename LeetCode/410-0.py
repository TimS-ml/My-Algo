'''
# Code Explain:
- Time complexity: O(N logS)
- Space complexity: O(1)

Same code in 1011
'''

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def min_subarrays_required(maxSum: int) -> int:
            currSum = 0
            splits = 0

            for element in nums:
                # Add element only if the sum doesn't exceed maxSum
                if currSum + element <= maxSum:
                    currSum += element
                else:
                    # If the element addition makes sum more than maxSum
                    # Increment the splits required and reset sum
                    currSum = element
                    splits += 1

            # Return the number of subarrays, which is the number of splits + 1
            return splits + 1

        # Define the left and right boundary of binary search
        left = max(nums)
        right = sum(nums)
        while left <= right:
            # Find the mid value
            maxSum = (left + right) // 2

            # Find the minimum splits. If splits is less than
            # or equal to m move towards left i.e., smaller values
            if min_subarrays_required(maxSum) <= m:
                right = maxSum - 1
                ans = maxSum
            else:
                # Move towards right if splits is more than m
                left = maxSum + 1

        return ans
