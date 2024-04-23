class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    dic = {}  # val: idx
    for i in range(len(nums)):
      if target - nums[i] in dic:
        return [i, dic[target - nums[i]]]
      else:
        dic[nums[i]] = i

