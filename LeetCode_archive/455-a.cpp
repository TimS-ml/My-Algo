/*
# Code Explain:
- Time complexity: O(nlogn + mlogm) -> sort
- Space complexity: O(m + n)

- give each child at most one cookie
- feed the lessest greed factor child first
*/

#include <iostream>
#include <unordered_map>
#include <vector>
// using std::unordered_map;
using std::vector;
using namespace std;

class Solution {
public:
  int findContentChildren(vector<int>& g, vector<int>& s) {
    // g: child, s: cookie
    sort(g.begin(), g.end());
    sort(s.begin(), s.end());

    int i = 0, j = 0;
    while (i < g.size() && j < s.size()) {
      // the lessest greed factor child can get the cookie
      if (g[i] <= s[j]) {
        i++;
      }
      j++;  // next cookie, no matter the child can get it or not
    }

    return i;
  }
};

int main() {
  Solution sol;

  // vector<int> kids = {1, 2, 3};
  // vector<int> cookies = {1, 1};

  vector<int> kids = {1, 2};
  vector<int> cookies = {1, 2, 3};

  int result = sol.findContentChildren(kids, cookies);
  cout << result << endl;

  // vector<int> result = sol.xxx;
  // for (int i : result) {
  //   cout << i << endl;
  // }
  return 0;
};
