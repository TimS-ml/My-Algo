/*
# Code Explain:
- Time complexity: O()
- Space complexity: O()

- Each child must have at least one candy. -> init all to 1
- Children with a higher rating (x>y) get more candies than their neighbors.
  - neighbor: left and right

# case
.... 2, 2 -> since 2nd '2' is not larger than 1st '2', so it should be 1 candy

*/

#include <iostream>
// #include <unordered_map>
#include <fstream>
#include <functional>
#include <numeric>
#include <sstream>
#include <vector>
// using std::unordered_map;
// using std::vector;
// using std::accumulate;
using namespace std;

class Solution {
public:
  int candy(vector<int> &r) {
    // r: ratings
    int sz = r.size();
    if (sz < 2) {
      return sz;
    }

    // https://www.geeksforgeeks.org/vector-in-cpp-stl/
    vector<int> num(sz, 1);
    // starting from 1, number of iter = sz -1
    // since all init with 1, so no need to do the value check
    // case: r = 1, 2; num = 1, 1;
    // otherwise the case could be:
    // case: r = 1, 2; num = 1, 3; -> no need to add
    for (int i = 1; i < sz; ++i) {
      // check if left one is smaller
      if (r[i] > r[i - 1]) {
        num[i] = max(num[i], num[i - 1] + 1);
        // num[i] = num[i-1] + 1;
      }
    }

    // starting from -1 idx (sz-2) to 0, number of iter = sz -1
    // check if right one is smaller
    // IMPORTANT: need to check if no need to add 1
    // case: r = 2, 1; num = 1, 1;
    // case: r = 2, 1; num = 1, 1;
    for (int i = sz - 2; i >= 0; --i) {
      if (r[i] > r[i + 1]) {
        num[i] = max(num[i], num[i + 1] + 1);
      }
    }

    // accumulate: first, last, init
    return accumulate(num.begin(), num.end(), 0);
  }
};

using SolutionFunc = function<int(vector<int> &)>;

SolutionFunc currentSolution;

int main() {
  Solution sol;
  currentSolution = bind(&Solution::candy, &sol, placeholders::_1);

  ifstream inputFile("135.txt");

  if (!inputFile.is_open()) {
    cout << "Error opening file" << endl;
    return 1;
  }

  string line;
  int testCase = 1;

  while (getline(inputFile, line)) {
    istringstream iss1(line);
    vector<int> in1;
    int num;

    while (iss1 >> num) {
      in1.push_back(num);
    }

    getline(inputFile, line);
    istringstream iss3(line);
    int expectedAnswer;
    iss3 >> expectedAnswer;

    int result = currentSolution(in1);
    cout << "Test Case " << testCase << ": " << result << ", "
         << (result == expectedAnswer ? "Correct" : "Wrong") << endl;

    testCase++;
  }

  inputFile.close();
  return 0;
}
