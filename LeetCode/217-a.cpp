/*
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(N)

simply return nums.size() > set<int>(nums.begin(), nums.end()).size();
*/

#include <iostream>
#include <map>
#include <vector>
#include <typeinfo>
using namespace std;

class Solution {
public:
  // using set
  bool containsDuplicate(vector<int> &nums) {
    map<int, int> hash;
    for (int i : nums) hash[i]++;

    bool flag = false;
    // for (auto i : hash){
      // string s = typeid(i).name();
      // cout << "type of i in hash: " << s << endl;
    for (pair<int, int> i : hash){
      if (i.second >= 2)
        return true;
    }
    return flag;
  }

  // using sort
  bool containsDuplicate_2(vector<int> &nums) {
    sort(nums.begin(), nums.end());
    bool flag = false;
    for (int i = 0; i < nums.size() - 1; i++) {
      if (nums[i] == nums[i + 1])
        return true;
    }
    return flag;
  }
};

int main() {
  Solution sol;
  std::vector<int> v1{1, 1, 1, 3, 3, 4, 3, 2, 4, 2};
  bool ans = sol.containsDuplicate(v1);
  cout << ans << endl;
  return 0;
};

