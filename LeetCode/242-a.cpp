/*
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(1)  # sol 2

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
    if (s.length() != t.length())
      return false;

    int n = s.length();
    unordered_map<char, int> counts;
    for (int i = 0; i < n; i++) {
      counts[s[i]]++;
      counts[t[i]]--;
    }

    for (pair<char, int> c : counts)
      if (c.second)
        return false;

    return true;
  }

  // Since the problem statement says that "the string contains only lowercase
  // alphabets", we can simply use an array to simulate the unordered_map and
  // speed up the code.
  bool isAnagram_2(string s, string t) {
    if (s.length() != t.length())
      return false;

    int n = s.length();
    // unordered_map<char, int> counts;
    int counts[26] = {0};
    for (int i = 0; i < n; i++) {
      counts[s[i] - 'a']++;
      counts[t[i] - 'a']--;
    }

    for (int i = 0; i < 26; i++)
      if (counts[i])
        return false;

    return true;
  }
};

int main() {
  Solution sol;
  string s = "anagram";
  string t = "nagaram";
  // bool result = sol.isAnagram(s, t);
  bool result = sol.isAnagram_2(s, t);
  cout << result << endl;
  return 0;
};
