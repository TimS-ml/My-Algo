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
  // public:
  //   vector<vector<string>> groupAnagrams(vector<string> &strs) {
  //     unordered_map<string, vector<string>> mp;
  //     for (string s : strs) {
  //       string t = s;
  //       sort(t.begin(), t.end());
  //       mp[t].push_back(s);
  //     }

  //     vector<vector<string>> anagrams;
  //     for (auto p : mp) {
  //       anagrams.push_back(p.second);
  //     }
  //     return anagrams;
  //   }
  // };

public:
  vector<vector<string>> groupAnagrams(vector<string> &strs) {
    unordered_map<string, vector<string>> mp;
    for (string s : strs) {
      mp[strSort(s)].push_back(s);
    }
    vector<vector<string>> anagrams;
    for (auto p : mp) {
      anagrams.push_back(p.second);
    }
    return anagrams;
  }

private:
  string strSort(string s) {
    int counter[26] = {0};
    for (char c : s) {
      counter[c - 'a']++;
    }
    string t;
    for (int c = 0; c < 26; c++) {
      t += string(counter[c], c + 'a');
    }
    return t;
  }
};

int main() {
  Solution sol;

  // bool result = sol.xxx;
  // cout << result << endl;

  vector<string> strs = {"eat", "tea", "tan", "ate", "nat", "bat"};
  vector<vector<string>> result = sol.groupAnagrams(strs);
  for (int i = 0; i < result.size(); i++) {
    for (string c : result[i])
      cout << c << ' ';
    cout << endl;
  }
  return 0;
};
