#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
  vector<int> twoSum(vector<int> &nums, int target) {
    std::unordered_map<int, int> record;
    for (int i = 0; i != nums.size(); ++i) {
      auto found = record.find(nums[i]);
      if (found != record.end())
        return {found->second, i};
      record.emplace(target - nums[i], i);
    }
    return {-1, -1};
  }
};

int main() {
  vector<int> nums;
  int array[] = {2, 7, 11, 15};
  nums.insert(nums.begin(), array, array + 4);
  int target = 9;
  vector<int> ans = Solution().twoSum(nums, target);
  for (auto it = ans.begin(); it < ans.end(); it++)
    cout << ' ' << *it;
  return 0;
}
