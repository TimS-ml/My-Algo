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
  // 方法1: 使用指针，最直观的实现
  void merge_v1(vector<int> &nums1, int m, vector<int> &nums2, int n) {
    // 指向两个数组的最后一个有效元素
    int *p1 = &nums1[m - 1];      // nums1的末尾
    int *p2 = &nums2[n - 1];      // nums2的末尾
    int *pos = &nums1[m + n - 1]; // 合并后数组的末尾

    // 从后往前比较并放置元素
    while (p1 >= &nums1[0] && p2 >= &nums2[0]) {
      if (*p1 > *p2) {
        *pos = *p1;
        p1--;
      } else {
        *pos = *p2;
        p2--;
      }
      pos--;
    }

    // 处理nums2中剩余的元素
    while (p2 >= &nums2[0]) {
      *pos = *p2;
      pos--;
      p2--;
    }
  }

  // 方法2: 使用指针算术，更简洁
  void merge_v2(vector<int> &nums1, int m, vector<int> &nums2, int n) {
    int *p1 = nums1.data() + m - 1; // 直接获取数据指针
    int *p2 = nums2.data() + n - 1;
    int *pos = nums1.data() + m + n - 1;

    while (p1 >= nums1.data() && p2 >= nums2.data()) {
      *pos-- = (*p1 > *p2) ? *p1-- : *p2--;
    }

    while (p2 >= nums2.data()) {
      *pos-- = *p2--;
    }
  }

  // 方法3: 混合使用指针和索引
  void merge_v3(vector<int> &nums1, int m, vector<int> &nums2, int n) {
    int *base1 = nums1.data();
    int *base2 = nums2.data();

    int i = m - 1, j = n - 1, k = m + n - 1;

    while (i >= 0 && j >= 0) {
      *(base1 + k--) =
          (*(base1 + i) > *(base2 + j)) ? *(base1 + i--) : *(base2 + j--);
    }

    while (j >= 0) {
      *(base1 + k--) = *(base2 + j--);
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
