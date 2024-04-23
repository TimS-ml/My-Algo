/*
# Code Explain:
- Time complexity: O()
- Space complexity: O()

https://leetcode.com/problems/min-cost-climbing-stairs/solutions/3496292/memoization-tabulation-space-optimization-1-space-optimization-2-3-lines-code/
*/

#include <iostream>
#include <unordered_map>
#include <vector>
// using std::unordered_map;
// using std::vector;
using namespace std;

class Solution {
public:
  int minCostClimbingStairs(vector<int> &cost) {
    int n = cost.size();
    for (int i = 2; i < n; i++) {
      cost[i] += min(cost[i - 1], cost[i - 2]);
    }
    return min(cost[n - 1], cost[n - 2]);
  }
};

int main() {
  Solution sol;

  // bool result = sol.xxx;
  // cout << result << endl;

  // vector<int> result = sol.xxx;
  // for (int i : result) {
  //   cout << i << endl;
  // }
  return 0;
};
