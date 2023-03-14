/*
# Code Explain:
- Time complexity: O()
- Space complexity: O()

*/

#include <iostream>
#include <unordered_map>
#include <vector>
// using std::unordered_map;
// using std::vector;
using namespace std;

class Solution {
public:
  bool isAnagram(string s, string t) {
    if (s.length() != t.length()) return false;

    int n = s.length();
    unordered_map<char, int> counts;
    for (int i = 0; i<n; i++) {
      counts[s[i]]++;
      counts[t[i]]--;
    }
    
    for (pair<char, int> c : counts)
      if (c.second) return false;

    return true;
  }
};

int main() {
  Solution sol;
  string s = "anagram";
  string t = "nagaram";
  bool result = sol.isAnagram(s, t);
  cout << result << endl;
  return 0;
};
