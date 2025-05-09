/*
# Code Explain:
- Time complexity: O(NlogN) - due to sorting
- Space complexity: O(1) - we only use a constant amount of extra space
*/

#include <iostream>
#include <vector>
#include <fstream>
#include <functional>
#include <algorithm>
using namespace std;

class Solution {
public:
    int findMinArrowShots(vector<vector<int>>& points) {
        if (points.empty()) return 0;
        int n = points.size();

        // Sort by end position
        sort(points.begin(), points.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[1] < b[1];
        });

        int arrows = 1; // Start with one arrow
        int arrow_pos = points[0][1]; // Position of the first arrow

        for (int i = 1; i < n; i++) {
            // If current balloon starts after the arrow position
            // We need a new arrow
            if (points[i][0] > arrow_pos) {
                arrows++;
                arrow_pos = points[i][1];
            }
        }

        return arrows;
    }
    
    // Alternative solution sorting by start position
    int findMinArrowShots_2(vector<vector<int>>& points) {
        if (points.empty()) return 0;
        int n = points.size();
        
        // Sort by start position
        sort(points.begin(), points.end());
        
        int arrows = 1;
        // Track the overlap region
        int curr_end = points[0][1];
        
        for (int i = 1; i < n; i++) {
            // If current balloon starts after the end of previous overlap
            if (points[i][0] > curr_end) {
                arrows++;
                curr_end = points[i][1];
            } else {
                // Update the overlap region
                curr_end = min(curr_end, points[i][1]);
            }
        }
        
        return arrows;
    }
};

using SolutionFunc = function<int(vector<vector<int>>&)>;

SolutionFunc currentSolution;

int main() {
    Solution sol;
    currentSolution = bind(&Solution::findMinArrowShots, &sol, placeholders::_1);

    ifstream inputFile("452.txt");
    
    if (!inputFile.is_open()) {
        cout << "Error opening file" << endl;
        return 1;
    }

    int testCase = 1;
    int n;
    
    while (inputFile >> n) {
        if (n == 0) break; // End of file

        vector<vector<int>> points(n, vector<int>(2));
        for (int i = 0; i < n; i++) {
            inputFile >> points[i][0] >> points[i][1];
        }

        int expected;
        inputFile >> expected;

        int result = currentSolution(points);
        cout << "Test Case " << testCase << ": " << result 
             << ", " << (result == expected ? "Correct" : "Wrong") << endl;
        
        testCase++;
    }

    inputFile.close();
    return 0;
}
