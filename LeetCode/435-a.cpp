/*
# Code Explain:
- Time complexity: O()
- Space complexity: O()

*/

#include <iostream>
// #include <unordered_map>
#include <fstream>
#include <vector>
// #include <sstream>
#include <functional>
// #include <numeric>
#include <algorithm>
// using std::unordered_map;
// using std::vector;
using namespace std;

class Solution {
public:
  int eraseOverlapIntervals(vector<vector<int>> &intervals) {
    if (intervals.empty())
      return 0;
    int n = intervals.size();

    // sort by end
    // sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const
    // vector<int>& b) {
    //     return a[1] < b[1];
    // });
    // Using C++20 ranges for sorting
    ranges::sort(intervals, {},
                 [](const auto &interval) { return interval[1]; });

    int removed = 0; // the number of removed intervals
    int prev_end = intervals[0][1];

    for (int i = 1; i < n; i++) {
      if (intervals[i][0] < prev_end) {
        removed++;
      } else {
        prev_end = intervals[i][1];
      }
    }

    return removed;
  }
};

using SolutionFunc = function<int(vector<vector<int>> &)>;

SolutionFunc currentSolution;

int main() {
  Solution sol;
  currentSolution =
      bind(&Solution::eraseOverlapIntervals, &sol, placeholders::_1);

  ifstream inputFile("435.txt");

  if (!inputFile.is_open()) {
    cout << "Error opening file" << endl;
    return 1;
  }

  int testCase = 1;
  int n;

  while (inputFile >> n) {
    if (n == 0)
      break; // End of file

    vector<vector<int>> intervals(n, vector<int>(2));
    for (int i = 0; i < n; i++) {
      inputFile >> intervals[i][0] >> intervals[i][1];
    }

    int expected;
    inputFile >> expected;

    int result = currentSolution(intervals);
    cout << "Test Case " << testCase << ": " << result << ", "
         << (result == expected ? "Correct" : "Wrong") << endl;

    testCase++;
  }

  inputFile.close();
  return 0;
}
