'''
Find all of its contiguous subarrays whose product is less than the target number

# Code Explain:
- Time complexity: O(n^3)
they believe substr generation will cause n^2
- Space complexity: O(n^3)

# Pros and Cons and Notation:
same as bp06
this time we are calc sub arr product instead of sum

careful, this is an unsorted array

if a * b * ... * h < target
then any contiguous subarr's product in a~h should < target
but we'd better fix one boundary

in find_subarrays_brute, fix l side, gen subarr from l side
in find_subarrays, fix r side, gen subarr from r side
'''

from collections import deque


def find_subarrays_brute(arr, target):
    ans = []
    for i in range(len(arr)):
        if arr[i] < target:
            temp_mul = arr[i]
            temp_li = [arr[i]]
            ans.append(temp_li.copy())
            # print(temp_li, ans)

            for j in range(i+1, len(arr)):
                temp_mul *= arr[j]
                if temp_mul < target:
                    temp_li.append(arr[j])
                    ans.append(temp_li.copy())
                    # print(temp_li, ans)
                else:
                    break
    return ans
            
def find_subarrays_brute2(arr, target):
    ans = []
    for i in range(len(arr)):
        if arr[i] < target:
            temp_mul = arr[i]
            temp_li = [arr[i]]
            
            # r will stop at: [1] end of loop, [2] prod *= arr[r+1] > j
            for j in range(i+1, len(arr)):
                temp_mul *= arr[j] 

                # if   a * b * ... * f > target
                # then a * b * ... * f * g > target
                if temp_mul >= target:
                    break
                
                temp_li.append(arr[j])

            while len(temp_li) > 0:  # make sure not add []
                ans.append(temp_li.copy())
                # print(temp_li, ans)
                temp_li.pop()
    return ans


def find_subarrays(arr, target):
    ans = []
    l, r = 0, 0
    temp_mul = 1

    while r < len(arr):
        temp_mul *= arr[r]

        # if   c * ... * f > target
        # then c * ... * f * g > target
        # which means 'l' doesn't need to move left
        while temp_mul >= target and l < r:
            temp_mul /= arr[l]
            l += 1

        # !! since we fix r side, if we generate subarr from l side, there will be duplicates
        # if from l side: [2, 5] will add [[2], [2, 5]]
        #              [2, 5, 3] will have [[2], [2, 5], [2, 5, 3]]
        # if from r side: [2, 5] will add [[5], [5, 2]]
        #              [2, 5, 3] will have [[3], [3, 5], [3, 5, 2]]
        temp_li = deque()  # popleft
        for i in range(r, l - 1, -1):
            temp_li.appendleft(arr[i])
            ans.append(list(temp_li))

        r += 1

    return ans


def main():
    print(find_subarrays([2, 5, 3, 10], 300))
    print(find_subarrays_brute([2, 5, 3, 10], 300))
    print(find_subarrays_brute2([2, 5, 3, 10], 300))
    # print(find_subarrays([2, 2, 5, 3, 10], 0))
    # print(find_subarrays([8, 2, 6, 5], 50))


main()
