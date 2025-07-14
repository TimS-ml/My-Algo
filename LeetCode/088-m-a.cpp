/*
# Code Explain:
- Time complexity: O()
- Space complexity: O()

*/

#include <algorithm>
#include <fstream>
#include <functional>
#include <iostream>
#include <sstream>
#include <vector>
using namespace std;

class Solution {
public:
  void merge(vector<int> &nums1, int m, vector<int> &nums2, int n) {
    // m-- returns m; --m returns m-1
    int pos = m-- + n-- - 1;
    while (m >= 0 && n >= 0) {
      if (nums1[m] >= nums2[n]) {
        nums1[pos] = nums1[m];
        pos--;
        m--;
      } else {
        nums1[pos] = nums2[n];
        pos--;
        n--;
      }
    }
    while (n >= 0) {
      nums1[pos] = nums2[n];
      pos--;
      n--;
    }
  }
};

// Function to parse a line of space-separated integers
vector<int> parseInputArray(const string &input_str) {
  vector<int> result;
  if (input_str.empty()) {
    return result;
  }

  stringstream ss(input_str);
  int num;
  while (ss >> num) {
    result.push_back(num);
  }
  return result;
}

using SolutionFunc = function<void(vector<int> &, int, vector<int> &, int)>;

SolutionFunc currentSolution;

int main() {
  Solution sol;
  currentSolution = bind(&Solution::merge, &sol, placeholders::_1,
                         placeholders::_2, placeholders::_3, placeholders::_4);

  ifstream inputFile("088.txt");

  if (!inputFile.is_open()) {
    cout << "Error opening file" << endl;
    return 1;
  }

  int testCase = 1;
  string line;

  while (getline(inputFile, line)) {
    if (line == "0")
      break; // End of file

    // Parse m and n
    int m, n;
    stringstream ss(line);
    ss >> m >> n;

    // Read nums1 and nums2
    string nums1_line, nums2_line;
    getline(inputFile, nums1_line);
    getline(inputFile, nums2_line);

    // Parse nums1 and nums2
    vector<int> nums1 = parseInputArray(nums1_line);
    vector<int> nums2 = parseInputArray(nums2_line);

    // Read expected result
    string expected_line;
    getline(inputFile, expected_line);
    vector<int> expected = parseInputArray(expected_line);

    // Create a copy of nums1 for testing
    vector<int> nums1_copy = nums1;

    // Apply the solution
    currentSolution(nums1_copy, m, nums2, n);

    // Check if the result matches expected
    bool result_correct = nums1_copy == expected;
    cout << "Test Case " << testCase << ": "
         << (result_correct ? "Correct" : "Wrong") << endl;

    if (!result_correct) {
      cout << "  Expected: ";
      for (size_t i = 0; i < expected.size(); ++i) {
        cout << expected[i];
        if (i < expected.size() - 1)
          cout << " ";
      }
      cout << endl;

      cout << "  Got: ";
      for (size_t i = 0; i < nums1_copy.size(); ++i) {
        cout << nums1_copy[i];
        if (i < nums1_copy.size() - 1)
          cout << " ";
      }
      cout << endl;
    }

    testCase++;
  }

  inputFile.close();
  return 0;
}
