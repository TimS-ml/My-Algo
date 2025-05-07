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
#include <vector>
#include <fstream>
#include <sstream>
#include <functional>
#include <numeric>
// using std::unordered_map;
// using std::vector;
// using std::accumulate;
using namespace std;

class Solution {
public:
  int candy(vector<int>& ratings) {
    int size = ratings.size(); 
    if (size < 2) return size;  // corner case, one kid

    vector<int> num(size, 1);  // init 1 candy for each kid
    
    // left to right
    for (int i = 1; i < size; i++) {
      if (ratings[i] > ratings[i - 1]) {
        // NOTE: since we init all to 1, so there's no need for comparision
        num[i] = num[i - 1] + 1;
      }
    }

    // right to left
    for (int i = size - 1; i > 0; i--) {
      if (ratings[i - 1] > ratings[i]) {
        num[i - 1] = max(num[i - 1], num[i] + 1);
      }
    }

    return accumulate(num.begin(), num.end(), 0);
  }
};

using SolutionFunc = function<int(vector<int>&)>;

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
        cout << "Test Case " << testCase << ": " << result 
             << ", " << (result == expectedAnswer ? "Correct" : "Wrong") << endl;
        
        testCase++;
    }

    inputFile.close();
    return 0;
}
