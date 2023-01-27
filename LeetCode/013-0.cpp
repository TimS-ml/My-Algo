#include <iostream>
#include <unordered_map>

using namespace std;
using std::unordered_map;

class Solution {
public:
  int romanToInt(string s) {
    unordered_map<char, int> mp = {{'M', 1000}, {'D', 500}, {'C', 100},
                                   {'L', 50},   {'X', 10},  {'V', 5},
                                   {'I', 1}};
    int ans = mp[s.back()]; // s.back() got the last digit
    cout << "init ans:" << ans << endl;

    // iter through len(s) - 1
    for (int i = 0; i < s.size() - 1; i++) {
      if (mp[s[i]] < mp[s[i + 1]])
        ans -= mp[s[i]];
      else
        ans += mp[s[i]];
    }
    return ans;
  }
};

int main() {
  Solution sol;
  string s = "MCMXCIV"; // 1994
  int result = sol.romanToInt(s);
  cout << result << endl;
  return 0;
};
