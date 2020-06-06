// using map store char's index

#include <iostream>
#include <map>
#include <string.h>
#include <string>
using namespace std;

class Solution {
public:
  int lengthOfLongestSubstring(string s) {
    map<char, int> m;
    int maxLen = 0;
    int lastRepeatPos = -1;
    for (int i = 0; i < s.size(); i++) {
      if (m.find(s[i]) != m.end() && lastRepeatPos < m[s[i]])
        lastRepeatPos = m[s[i]];
      if (i - lastRepeatPos > maxLen)
        maxLen = i - lastRepeatPos;
      m[s[i]] = i;
    }
    return maxLen;
  }
};

int main() {
  string s = "pwwkew";
  int ans = Solution().lengthOfLongestSubstring(s);
  cout << ans << endl;
  return 0;
}
