/*
# Code Explain:
- Time complexity: O(nlogn + mlogm) -> sort
- Space complexity: O(m + n)

- give each child at most one cookie
- feed the lessest greed factor child first
*/

#include <iostream>
// #include <unordered_map>
#include <algorithm>
#include <fstream>
#include <functional>
#include <sstream>
#include <vector>
// using std::unordered_map;
// using std::vector;
using namespace std;

class Solution {
public:
  int findContentChildren(vector<int> &g, vector<int> &s) {
    // g: child, s: cookie
    sort(g.begin(), g.end());
    sort(s.begin(), s.end());

    // int i = 0, j = 0;
    size_t i = 0, j = 0;
    while (i < g.size() && j < s.size()) {
      // the lessest greed factor child can get the cookie
      if (g[i] <= s[j]) {
        i++;
      }
      j++; // next cookie, no matter the child can get it or not
    }

    return i;
  }
};

using SolutionFunc = function<int(vector<int> &, vector<int> &)>;

SolutionFunc currentSolution;

int main() {
  Solution sol;
  currentSolution = bind(&Solution::findContentChildren, &sol, placeholders::_1,
                         placeholders::_2);

  ifstream inputFile("455.txt");

  if (!inputFile.is_open()) {
    cout << "Error opening file" << endl;
    return 1;
  }

  string line;
  int testCase = 1;

  while (getline(inputFile, line)) {
    istringstream iss1(line);
    vector<int> in1, in2;
    int num;

    while (iss1 >> num) {
      in1.push_back(num);
    }

    getline(inputFile, line);
    istringstream iss2(line);
    while (iss2 >> num) {
      in2.push_back(num);
    }

    // int result = currentSolution(in1, in2);
    // cout << "Test Case " << testCase << ": " << result << endl;

    getline(inputFile, line);
    istringstream iss3(line);
    int expectedAnswer;
    iss3 >> expectedAnswer;

    int result = currentSolution(in1, in2);
    cout << "Test Case " << testCase << ": " << result << ", "
         << (result == expectedAnswer ? "Correct" : "Wrong") << endl;

    testCase++;
  }

  inputFile.close();
  return 0;
}
