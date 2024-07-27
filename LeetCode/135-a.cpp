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
#include <numeric>
#include <unordered_map>
#include <vector>
// using std::unordered_map;
// using std::vector;
using namespace std;

class Solution {
public:
  int candy(vector<int>& ratings) {
    int size = ratings.size(); 
    if (size < 2) return size;  // corner case, one kid 1 candy
    vector<int> num(size, 1);  // init all to 1
    
    for (int i = 1; i < size; i++) {
      if (ratings[i] > ratings[i - 1]) {
        num[i] = num[i - 1] + 1;
      }
    }

    for (int i = size - 1; i > 0; i--) {
      if (ratings[i - 1] > ratings[i]) {
        num[i - 1] = max(num[i - 1], num[i] + 1);
      }
    }

    return accumulate(num.begin(), num.end(), 0);
  }
};

int main() {
  Solution sol;

  // vector<int> ratings = {1, 0, 2};
  vector<int> ratings = {1, 2, 2};
  int result = sol.candy(ratings);
  cout << result << endl;

  // vector<int> result = sol.xxx;
  // for (int i : result) {
  //   cout << i << endl;
  // }
  return 0;
};
