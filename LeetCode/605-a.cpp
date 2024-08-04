/*
# Code Explain:
- Time complexity: O(N)
- Space complexity: O(1)
*/

#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
#include <functional>

using namespace std;

class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        // append 0 at the begin and end of the flowerbed
        flowerbed.insert(flowerbed.begin(), 0);
        flowerbed.push_back(0);

        int cnt = 0;
        // iter from 1 to len-1
        for (int i = 1; i < flowerbed.size() - 1; i++) {
            if (flowerbed[i - 1] == 0 && flowerbed[i] == 0 && flowerbed[i + 1] == 0) {
                flowerbed[i] = 1;
                cnt++;
            }
        }
        return cnt >= n;
    }
};

using SolutionFunc = function<bool(vector<int>&, int)>;

SolutionFunc currentSolution;

int main() {
    Solution sol;
    currentSolution = bind(&Solution::canPlaceFlowers, &sol, placeholders::_1, placeholders::_2);

    ifstream inputFile("605.txt");
    
    if (!inputFile.is_open()) {
        cout << "Error opening file" << endl;
        return 1;
    }

    string line;
    int testCase = 1;
    
    while (getline(inputFile, line)) {
        if (line.empty()) {
            break;  // End of file
        }

        istringstream iss(line);
        vector<int> flowerbed;
        int num;
        while (iss >> num) {
            flowerbed.push_back(num);
        }

        getline(inputFile, line);
        int n = stoi(line);

        getline(inputFile, line);
        bool expected = static_cast<bool>(stoi(line));

        bool result = currentSolution(flowerbed, n);
        cout << "Test Case " << testCase << ": " << (result ? "true" : "false")
             << ", " << (result == expected ? "Correct" : "Wrong") << endl;
        
        testCase++;
    }

    inputFile.close();
    return 0;
}
