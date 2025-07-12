/*
# Code Explain:
- Time complexity: O(|S|+|T|)
- Space complexity: O(1) - fixed size arrays for ASCII chars

This problem uses the sliding window technique with arrays to track character
frequencies. The key is to maintain a valid window that contains all characters
from target string.
*/

#include <algorithm>
#include <climits>
#include <fstream>
#include <functional>
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
    // Array-based approach similar to original C++ solution
    string minWindow(string s, string t) {
      unordered_map<char, int> missing_cnt;
      unordered_map<char, int> window;
      
      for (char cr : t) { missing_cnt[cr]++; }
      int found = 0;
      size_t l = 0, r = 0;
      int min_l = 0, min_sz = s.size() + 1;

      while (r < s.size()) {
        char cr = s[r];

        // if cr in missing_cnt
        if (missing_cnt.find(cr) != missing_cnt.end()) {
          window[cr]++;
          if (window[cr] == missing_cnt[cr]) found ++;
        }

        while (found == static_cast<int>(missing_cnt.size())) {
          int sz = r - l + 1;
          char cl = s[l];

          if (sz < min_sz) {
            min_l = l;
            min_sz = sz;
          }

          // if cl in missing_cnt
          if (missing_cnt.find(cl) != missing_cnt.end()) {
            window[cl]--;
            if (window[cl] < missing_cnt[cl]) found--;
          }
          l++;
        }
        r++; 
      }
      return min_sz > static_cast<int>(s.size()) ? "" : s.substr(min_l, min_sz);
    }
};

using SolutionFunc = function<string(string, string)>;
SolutionFunc currentSolution;

int main() {
    Solution sol;
    currentSolution = bind(&Solution::minWindow, &sol, placeholders::_1, placeholders::_2);

    ifstream inputFile("076.txt");
    
    if (!inputFile.is_open()) {
        cout << "Error opening file" << endl;
        return 1;
    }

    int testCase = 1;
    int n;
    
    while (inputFile >> n) {
        if (n == 0) break;

        string s, t, expected;
        inputFile >> s >> t >> expected;

        string result = currentSolution(s, t);
        cout << "Test Case " << testCase << ": '" << result 
             << "', " << (result == expected ? "Correct" : "Wrong") << endl;
        
        testCase++;
    }

    inputFile.close();
    return 0;
}
