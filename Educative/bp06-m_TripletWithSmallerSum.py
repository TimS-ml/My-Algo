'''
Count all triplets in it such that arr[i] + arr[j] + arr[k] < target where i, j, and k are three different indices

# Code Explain:
- Time complexity: O(n^2)
- Space complexity: O(n)



same as bp04
target_sum is given

since diff indices is ok, so do not skip duplicate

About that count += r-l:
-1, 1, 4 -> count += 3 (4-1)
    since if 1, 4 matches the case, then 1, 3 / 1, 2 also matches
    so, count += from arr[l] to all numbers<=arr[r]
-1, 2, 3
'''

def triplet_with_smaller_sum(arr, target_sum):
    def count_diff(target, subarr, f):
        # !! find the one that has the abs(diff) closest to 0
        # since this is a sorted array, we can use two pointers to do that
        l = 0
        r = len(subarr) - 1
        count = 0
        while l < r:
            # print(f, subarr[l], subarr[r])
            diff = target - subarr[l] - subarr[r]
            if diff > 0:
                # this is the edge cases
                # print(f, subarr[l], subarr[r])
                count += r-l
                l += 1
            else:
                r -= 1
        return count
    
    arr.sort()
    ans = 0
    for i in range(len(arr) - 2):
        ans += count_diff(target_sum - arr[i], arr[i+1:], arr[i])

    return ans


def main():
    # print(triplet_with_smaller_sum([-1, 0, 2, 3], 3))
    # print(triplet_with_smaller_sum([-1, -1, 4, 1], 5))
    # print(triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5))
    print(triplet_with_smaller_sum([-1, 1, 2, 3, 4], 5))


main()
