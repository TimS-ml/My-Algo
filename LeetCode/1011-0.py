'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

Same code in 410
'''
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def min_subarrays_required(maxSum: int) -> int:
            currSum = 0
            splits = 0
            
            for element in weights:
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
        left = max(weights)
        right = sum(weights)
        while left <= right:
            # Find the mid value
            maxSum = (left + right) // 2
            
            # Find the minimum splits. If splits is less than
            # or equal to days move towards left i.e., smaller values
            if min_subarrays_required(maxSum) <= days:
                right = maxSum - 1
                ans = maxSum
            else:
                # Move towards right if splits is more than days
                left = maxSum + 1
        
        return ans

