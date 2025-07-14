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
    
    // this is way faster: from 18ms to 3ms
    std::string minWindow_2(std::string s, std::string t) {
        if (s.empty() || t.empty()) return "";
        
        std::vector<int> target_count(128, 0);
        std::vector<bool> is_target(128, false);
        
        int required_chars = 0;
        
        for (char c : t) {
            if (!is_target[c]) {
                is_target[c] = true;
                required_chars++;
            }
            target_count[c]++;
        }
        
        std::vector<int> window_count(128, 0);
        int formed = 0;
        int l = 0;
        int min_l = 0;
        int min_sz = INT_MAX;
        
        for (int r = 0; r < s.size(); ++r) {
            char cr = s[r];
            window_count[cr]++;
            
            if (is_target[cr] && window_count[cr] == target_count[cr]) {
                formed++;
            }
            
            while (l <= r && formed == required_chars) {
                if (r - l + 1 < min_sz) {
                    min_sz = r - l + 1;
                    min_l = l;
                }
                
                char cl = s[l];
                window_count[cl]--;
                
                if (is_target[cl] && window_count[cl] < target_count[cl]) {
                    formed--;
                }
                l++;
            }
        }
        
        return min_sz == INT_MAX ? "" : s.substr(min_l, min_sz);
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
