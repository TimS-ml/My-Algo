# https://leetcode-cn.com/problems/permutations/
# https://medium.com/algorithms-and-leetcode/backtracking-e001561b9f28
# modify of ans1, this does has faster speed and low mem useage


class Solution:
    def permute(self, nums):
        def backtracking(temp, ans):
            print(temp)
            if len(nums) == len(temp):
                ans.append(list(temp))
            for i in range(len(nums)):
                if nums[i] in temp:
                    continue
                temp.append(nums[i])
                backtracking(temp, ans)
                # print('depth', len(temp))
                temp.pop()
        ans = []
        temp = []
        backtracking(temp, ans)
        return ans


nums = [1, 2, 3]
print(Solution().permute(nums))
