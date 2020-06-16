// HashMap
// https://www.programiz.com/java-programming/hashmap

import java.util.HashMap;

// import java.util.Hashtable;

class Solution {
  public int[] twoSum(int[] nums, int target) {
    int len = nums.length;
    HashMap<Integer, Integer> map = new HashMap<>();
    for (int i = 0; i < len; ++i) {
      final Integer value = map.get(nums[i]);
      if (value != null) {
        return new int[] {value, i};
      }
      map.put(target - nums[i], i);
    }
    return null;
  }
}

class Run {
  public static void main(String[] args) {
    int[] nums = new int[]{2, 7, 11, 15};
    int target = 9;
    Solution s = new Solution();
    int[] ans = s.twoSum(nums, target);
    for (int i = 0; i < ans.length; i++)
      System.out.println(ans[i]);
  }
}
