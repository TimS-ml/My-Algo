/*
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(1)
*/

#include <algorithm>
#include <fstream>
#include <functional>
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
  int maxProfit(vector<int> &prices) {
    int ans = 0;
    for (size_t i = 1; i < prices.size(); i++) {
      int gap = prices[i] - prices[i - 1];
      if (gap > 0) {
        ans += gap;
      }
    }
    return ans;
  }
};

using SolutionFunc = function<int(vector<int> &)>;

SolutionFunc currentSolution;

int main() {
  Solution sol;
  currentSolution = bind(&Solution::maxProfit, &sol, placeholders::_1);

  ifstream inputFile("122.txt");

  if (!inputFile.is_open()) {
    cout << "Error opening file" << endl;
    return 1;
  }

  int testCase = 1;
  int n;

  while (inputFile >> n) {
    if (n == 0)
      break; // End of file

    vector<int> prices(n);
    for (int i = 0; i < n; i++) {
      inputFile >> prices[i];
    }

    int expected;
    inputFile >> expected;

    int result = currentSolution(prices);
    cout << "Test Case " << testCase << ": " << result << ", "
         << (result == expected ? "Correct" : "Wrong") << endl;

    testCase++;
  }

  inputFile.close();
  return 0;
}
