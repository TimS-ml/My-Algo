# http: // www.runoob.com / python / python - func - set.html
# set(): unordered, not duplicate


class Solution:
    def containsDuplicate(self, nums) -> bool:
        return len(nums) != len(set(nums))


nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
print(Solution().containsDuplicate(nums))
