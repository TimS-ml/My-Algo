/*
# Code Explain:
- Time complexity: O(1)
- Space complexity: O(1)


Thoughts:
- [1] for add without carry: bit xor
- [2] for carry: or, then <<

Things to consider:
- neg value?
- when stop? -> carry is 0
- why unsigned int?

How to further improve?
- without using extra var
  - use a as [1]
  - use b as [2]

*/

#include <iostream>
#include <unordered_map>
#include <vector>
// using std::unordered_map;
// using std::vector;
using namespace std;

class Solution {
public:
  int getSum(int a, int b) {
    while (b != 0) {
      unsigned int carry = (unsigned int)(a & b) << 1;
      a = a ^ b;
      b = carry;
    }
    return a;
  }
};

int main() {
  Solution sol;

  // bool result = sol.xxx;
  // cout << result << endl;

  // vector<int> result = sol.xxx;
  // for (int i : result) {
  //   cout << i << endl;
  // }
  return 0;
};
