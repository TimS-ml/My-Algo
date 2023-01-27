#include <vector>
#include <unordered_map>
#include <iostream>
using std::unordered_map;
using std::vector;
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
  Solution sol;
  std::vector<int> v1{2, 7, 11, 15};
  // cout << sol.twoSum(v1, 9) << endl;
  vector<int> result = sol.twoSum(v1, 9);
  for (int i : result) {
    cout << i << endl;
  }

  // std::vector<int> v2{0, 4, 3, 0};
  // REQUIRE( (s.twoSum(v2, 0) == std::vector<int>{0, 3}) );

  // std::vector<int> v3{-3, 4, 3, 90};
  // REQUIRE( (s.twoSum(v3, 0) == std::vector<int>{0, 2}) );
  return 0;
};
