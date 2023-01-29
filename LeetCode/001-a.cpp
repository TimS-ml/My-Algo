#include <iostream>
#include <unordered_map>
#include <vector>
// using std::unordered_map;
// using std::vector;
using namespace std;

class Solution {
public:
  vector<int> twoSum(vector<int> &nums, int target) {
    unordered_map<int, int> indices;
    for (int i = 0; i < nums.size(); i++) {
      // .end returns an iterator to the end
      if (indices.find(target - nums[i]) != indices.end()) {
        return {indices[target - nums[i]], i};
      }
      indices[nums[i]] = i;
    }
    return {};
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
