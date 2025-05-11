/*
# Problem Description:
- You are given a string s
- We want to partition the string into as many parts as possible
- Each letter must appear in at most one part
- Return a list of integers representing the size of these parts
*/

#include <fstream>
#include <functional>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
  vector<int> partitionLabels(string s) {
    vector<int> ans;
    unordered_map<char, size_t> last_appear;
    for (size_t i = 0; i < s.length(); i++) {
      last_appear[s[i]] = i;
    }
    size_t start = 0, end = 0;
    for (size_t i = 0; i < s.length(); i++) {
      end = max(end, last_appear[s[i]]);
      if (i == end) {
        ans.push_back(end - start + 1);
        // ans.push_back(static_cast<int>(end - start + 1));  // convert back to int
        start = end + 1;
      }
    }
    return ans;
  }
};

using SolutionFunc = function<vector<int>(string)>;

SolutionFunc currentSolution;

int main() {
  Solution sol;
  currentSolution = bind(&Solution::partitionLabels, &sol, placeholders::_1);

  ifstream inputFile("763.txt");

  if (!inputFile.is_open()) {
    cout << "Error opening file" << endl;
    return 1;
  }

  int testCase = 1;
  string s;

  while (getline(inputFile, s)) {
    if (s.empty())
      break; // End of file

    string expectedLine;
    getline(inputFile, expectedLine);

    vector<int> expected;
    stringstream ss(expectedLine);
    string item;

    while (getline(ss, item, ',')) {
      expected.push_back(stoi(item));
    }

    vector<int> result = currentSolution(s);

    cout << "Test Case " << testCase << ": [";
    for (size_t i = 0; i < result.size(); i++) {
      cout << result[i];
      if (i < result.size() - 1)
        cout << ",";
    }
    cout << "], ";

    bool correct = (result.size() == expected.size());
    if (correct) {
      for (size_t i = 0; i < result.size(); i++) {
        if (result[i] != expected[i]) {
          correct = false;
          break;
        }
      }
    }

    cout << (correct ? "Correct" : "Wrong") << endl;

    testCase++;
  }

  inputFile.close();
  return 0;
}
