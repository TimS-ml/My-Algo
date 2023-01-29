#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <vector>
// using std::unordered_map;
// using std::vector;
using namespace std;

class Solution {
public:
  // Constant to make elements non-negative.
  // note that static and constexpr are completely independent of each other.
  // static defines the object's lifetime during execution; constexpr specifies
  // that the object should be available during compilation. Compilation and
  // execution are disjoint and discontiguous, both in time and space. So once
  // the program is compiled, constexpr is no longer relevant.
  static constexpr int K = 1000;

  bool uniqueOccurrences(vector<int> &arr) {
    // integers in the array will always be in the range [-1000, 1000]. This range is of length 2000
    vector<int> freq(2 * K + 1);

    // Store the frequency of elements in the unordered map.
    for (int num : arr) {
      freq[num + K]++;
    }

    // Sort the frequency count.
    sort(freq.begin(), freq.end());

    // If the adjacent freq count is equal, then the freq count isn't unique.
    for (int i = 0; i < 2 * K; i++) {
      if (freq[i] && freq[i] == freq[i + 1]) {
        return false;
      }
    }

    // If all the elements are traversed, it implies frequency counts are
    // unique.
    return true;
  }
  bool uniqueOccurrences_2(vector<int>& arr) {
      // Store the frequency of elements in the unordered map.
      unordered_map<int, int> freq;
      for (int num : arr) {
          freq[num]++;
      }
      
      // Store the frequency count of elements in the unordered set.
      unordered_set<int> freqSet;
      for (auto [key, value] : freq) {
          freqSet.insert(value);
      }
      
      // If the set size is equal to the map size, 
      // It implies frequency counts are unique.
      return freqSet.size() == freq.size();
  }
};

int main() { 
  Solution sol;
  std::vector<int> v1{1, 1, 2, 3, 3, 3};
  bool result = sol.uniqueOccurrences_2(v1);
  cout << result << endl;
  return 0; 
};
