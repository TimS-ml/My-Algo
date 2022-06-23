'''
Given an array of unsorted numbers, find all unique triplets in it that add up to zero

# Code Explain:
- Time complexity: O(n^2)
- Space complexity: O(n)

lc 015, lc 018
'''


def search_triplets(nums):
    nums.sort()
    ans = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        target = 0 - nums[i]
        start, end = i + 1, len(nums) - 1
        # aggregate two pointers in one loop
        while start < end:
            if nums[start] + nums[end] > target:
                end -= 1
            elif nums[start] + nums[end] < target:
                start += 1
            else:
                ans.append([nums[i], nums[start], nums[end]])
                # move 2 pointers to avoid duplicate ans
                # think about case: [-1, 0, 0, 0 , 1, 1]
                end -= 1
                start += 1
                while start < end and nums[end] == nums[end + 1]:
                    end -= 1
                while start < end and nums[start] == nums[start - 1]:
                    start += 1
    return ans


def main():
    print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
    # print(search_triplets([-5, 2, -1, -2, 3]))


main()
