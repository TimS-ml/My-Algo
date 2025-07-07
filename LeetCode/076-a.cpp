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
        vector<int> chars(128, 0);    // target char frequency array
        vector<bool> flag(128, false); // target char existence flag
        
        // Initialize target character requirements
        for (size_t i = 0; i < t.size(); ++i) {
            flag[t[i]] = true;
            ++chars[t[i]];
        }

        int cnt = 0;              // total chars satisfied count
        int left = 0;
        int min_start = 0;
        int min_len = s.size() + 1;
        
        for (size_t right = 0; right < s.size(); ++right) {
            // Expand window: add current char
            if (flag[s[right]]) {
                if (--chars[s[right]] >= 0) {
                    ++cnt;  // only count when requirement not exceeded
                }
                
                // Contract window when all requirements met
                while (cnt == static_cast<int>(t.size())) {
                    // Update minimum window if current is smaller
                    if (static_cast<int>(right) - left + 1 < min_len) {
                        min_start = left;
                        min_len = static_cast<int>(right) - left + 1;
                    }
                    
                    // Remove leftmost char from window
                    if (flag[s[left]] && ++chars[s[left]] > 0) {
                        --cnt;
                    }
                    ++left;
                }
            }
        }
        
        return min_len > static_cast<int>(s.size()) ? "" : s.substr(min_start, min_len);
    }

    // Dictionary-based approach for comparison
    string minWindow_2(string s, string t) {
        unordered_map<char, int> need;    // target char frequency map
        unordered_map<char, int> window;  // current window frequency map
        
        // Initialize target character requirements
        for (char c : t) {
            need[c]++;
        }
        
        size_t left = 0, right = 0;
        int valid = 0;            // number of unique chars with satisfied frequency
        int min_start = 0;
        int min_len = INT_MAX;
        
        while (right < s.size()) {
            char c = s[right];
            right++;
            
            // Expand window: add current char
            if (need.count(c)) {
                window[c]++;
                if (window[c] == need[c]) {
                    valid++;
                }
            }
            
            // Contract window when all requirements met
            while (static_cast<size_t>(valid) == need.size()) {
                // Update minimum window if current is smaller
                if (static_cast<int>(right - left) < min_len) {
                    min_start = left;
                    min_len = right - left;
                }
                
                // Remove leftmost char from window
                char d = s[left];
                left++;
                if (need.count(d)) {
                    if (window[d] == need[d]) {
                        valid--;
                    }
                    window[d]--;
                }
            }
        }
        
        return min_len == INT_MAX ? "" : s.substr(min_start, min_len);
    }

    // Optimized array approach with char counting
    string minWindow_3(string s, string t) {
        vector<int> target_freq(128, 0);  // target char frequency
        vector<int> window_freq(128, 0);  // window char frequency
        int required_chars = 0;           // number of unique chars in target
        
        // Initialize target character requirements
        for (char c : t) {
            if (target_freq[c] == 0) {
                required_chars++;
            }
            target_freq[c]++;
        }
        
        size_t left = 0, right = 0;
        int formed = 0;           // number of unique chars with satisfied frequency
        int min_start = 0;
        int min_len = INT_MAX;
        
        while (right < s.size()) {
            char c = s[right];
            window_freq[c]++;
            
            // Check if frequency requirement met for this char
            if (target_freq[c] > 0 && window_freq[c] == target_freq[c]) {
                formed++;
            }
            
            // Contract window when all requirements met
            while (left <= right && formed == required_chars) {
                // Update minimum window if current is smaller
                if (static_cast<int>(right - left + 1) < min_len) {
                    min_start = left;
                    min_len = right - left + 1;
                }
                
                // Remove leftmost char from window
                char d = s[left];
                window_freq[d]--;
                if (target_freq[d] > 0 && window_freq[d] < target_freq[d]) {
                    formed--;
                }
                left++;
            }
            right++;
        }
        
        return min_len == INT_MAX ? "" : s.substr(min_start, min_len);
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
