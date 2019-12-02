    def backtracking(self, nums, temp, ans, used):
        if len(temp) == len(nums):
            ans.append(list(temp))
        for i in range(len(nums)):
            if used[i] or i>0 and nums[i]==nums[i-1] and not used[i-1]:
                continue
            temp.append(nums[i])
            used[i] = True  # track visit
            self.backtracking(nums, temp, ans, used)
            used[i] = False
            temp.pop()