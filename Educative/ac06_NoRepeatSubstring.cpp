using namespace std;

#include <iostream>
#include <string>
#include <unordered_map>

class NoRepeatSubstring {
 public:
  static int findLength(const string& str) {
    int windowStart = 0, maxLength = 0;
    unordered_map<char, int> charIndexMap;
    // try to extend the range [windowStart, windowEnd]
    for (int windowEnd = 0; windowEnd < str.length(); windowEnd++) {
      char rightChar = str[windowEnd];
      // if the map already contains the 'rightChar', shrink the window from the beginning so that
      // we have only one occurrence of 'rightChar'
      if (charIndexMap.find(rightChar) != charIndexMap.end()) {
        // this is tricky; in the current window, we will not have any 'rightChar' after its
        // previous index and if 'windowStart' is already ahead of the last index of 'rightChar',
        // we'll keep 'windowStart'
        windowStart = max(windowStart, charIndexMap[rightChar] + 1);
      }
      charIndexMap[rightChar] = windowEnd;  // insert the 'rightChar' into the map
      maxLength =
          max(maxLength, windowEnd - windowStart + 1);  // remember the maximum length so far
    }

    return maxLength;
  }
};

int main(int argc, char* argv[]) {
  cout << "Length of the longest substring: " << NoRepeatSubstring::findLength("aabccbb") << endl;
  cout << "Length of the longest substring: " << NoRepeatSubstring::findLength("abbbb") << endl;
  cout << "Length of the longest substring: " << NoRepeatSubstring::findLength("abccde") << endl;
}
