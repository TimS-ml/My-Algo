'''
Given a set of positive numbers, find if we can partition it into two subsets such that the sum of elements in both subsets is equal.

# Code Explain:
- Time complexity: O(2^N)
- Space complexity: O(N)

# Pros and Cons and Notation:
important: 
- the two subsets have the sum of sum(num)/2
- you only need to find one subset that sum(subset) = sum(num)/2

basic solution
for each number 'i' 
  create a new set which INCLUDES number 'i' if it does not exceed 'S/2', and recursively 
      process the remaining numbers
  create a new set WITHOUT number 'i', and recursively process the remaining items 
return true if any of the above sets has a sum equal to 'S/2', otherwise return false

Top down
[1] Base State
[2] State Transfer Equation => idx from idx+1 (top down)
[3] Initialize Conditions
[4] State Compression (optional)
[5] Terminate Conditions

I need 2-dim cache: sum (can/cannot achieve curr_sum from [0, s/2]) and capacity(total number of choose <= len/2)
To consider all var in `num`, the range of capacity should in [0, len(num)]
'''


def can_partition(num):
    s = sum(num)

    if s % 2 != 0:
        return False

    cache = [[-1 for _ in range(int(s / 2) + 1)] for _ in range(len(num))]

    def top_down_dp(cache, idx, curr_sum):
        if curr_sum == 0:
            return 1

        if idx >= len(num):
            return 0

        if cache[idx][curr_sum] == -1:
            if num[idx] <= curr_sum:
                # include curr idx
                if top_down_dp(cache, idx + 1, curr_sum - num[idx]):
                    cache[idx][curr_sum] = 1
                    return 1

            # not include curr idx
            cache[idx][curr_sum] = top_down_dp(cache, idx + 1, curr_sum)

        return cache[idx][curr_sum]
    
    if top_down_dp(cache, 0, int(s / 2)):
        return True
    else:
        return False


def main():
    print(str(can_partition([1, 2, 3, 4])))
    print(str(can_partition([1, 1, 3, 4, 7])))  # [1,3,4] and [1,7]
    print(str(can_partition([2, 3, 4, 6])))


main()
