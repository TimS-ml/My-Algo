/*
# LeetCode 167. Two Sum II - Input Array Is Sorted
# Time complexity:
# Space complexity:

*/

#include <algorithm>
#include <fstream>
#include <functional>
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
  vector<int> twoSum(vector<int> &numbers, int target) {
    int l = 0, r = numbers.size() - 1, sum;
    while (l < r) {
      sum = numbers[l] + numbers[r];
      if (sum == target) {
        return {l + 1, r + 1};
      } else if (sum < target) {
        ++l;
      } else {
        --r;
      }
    }
    return {};
  }
};

using SolutionFunc = function<vector<int>(vector<int> &, int)>;

SolutionFunc currentSolution;

int main() {
  Solution sol;
  currentSolution =
      bind(&Solution::twoSum, &sol, placeholders::_1, placeholders::_2);

  ifstream inputFile("167.txt");

  if (!inputFile.is_open()) {
    cout << "Error opening file" << endl;
    return 1;
  }

  int testCase = 1;
  int n;

  while (inputFile >> n) {
    if (n == 0)
      break; // End of file

    vector<int> numbers(n);
    for (int i = 0; i < n; i++) {
      inputFile >> numbers[i];
    }

    int target;
    inputFile >> target;

    vector<int> expected(2);
    inputFile >> expected[0] >> expected[1];

    vector<int> result = currentSolution(numbers, target);
    cout << "Test Case " << testCase << ": [" << result[0] << "," << result[1]
         << "], " << (result == expected ? "Correct" : "Wrong") << endl;

    testCase++;
  }

  inputFile.close();
  return 0;
}
