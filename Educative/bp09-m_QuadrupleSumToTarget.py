'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

lc 018 and bp04
'''


def search_quadruplets(nums, target):
    quadruplets = []
    nums.sort()

    def search_triplets(subNums, triplets_target):
        ans = []
    
        for i in range(len(subNums) - 2):
            if i > 0 and subNums[i] == subNums[i - 1]:
                continue
            subTarget = triplets_target - subNums[i]
            start, end = i + 1, len(subNums) - 1
            # aggregate two pointers in one loop
            while start < end:
                if subNums[start] + subNums[end] > subTarget:
                    end -= 1
                elif subNums[start] + subNums[end] < subTarget:
                    start += 1
                else:
                    # triplets_target = target - nums[i]
                    ans.append([target - triplets_target, 
                                subNums[i], 
                                subNums[start], subNums[end]])
                    # move 2 pointers to avoid duplicate ans
                    # think about case: [-1, 0, 0, 0 , 1, 1]
                    end -= 1
                    start += 1
                    while start < end and subNums[end] == subNums[end + 1]:
                        end -= 1
                    while start < end and subNums[start] == subNums[start - 1]:
                        start += 1
        return ans

    for i in range(len(nums) - 3):
        subAns = search_triplets(nums[i+1:], target - nums[i])
        # print(subAns)
        quadruplets += subAns
    return quadruplets


def main():
    print(search_quadruplets([4, 1, 2, -1, 1, -3], 1))
    print(search_quadruplets([2, 0, -1, 1, -2, 2], 2))


main()
