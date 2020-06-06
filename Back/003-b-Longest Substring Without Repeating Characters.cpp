// no map version

#include <iostream>
#include <string.h>
#include <string>
using namespace std;

class Solution {
public:
  int lengthOfLongestSubstring(string s) {
    const int MAX_CHARS = 256;
    int m[MAX_CHARS];
    memset(m, -1, sizeof(m));

    int maxLen = 0;
    int lastRepeatPos = -1;
    for (int i = 0; i < s.size(); i++) {
      if (m[s[i]] != -1 && lastRepeatPos < m[s[i]])
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
