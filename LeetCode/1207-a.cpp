#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <vector>
// using std::unordered_map;
// using std::vector;
using namespace std;

class Solution {
public:
  // https://stackoverflow.com/questions/45987571/difference-between-constexpr-and-static-constexpr-global-variable
  static constexpr int K = 1000;

  bool uniqueOccurrences(vector<int> &arr) {
    // !!! using array instead of hash set to count occurences !!!
    // integers in the array will always be in the range [-1000, 1000]. This
    // range is of length 2000
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

  // We can also note that the array length is limited to 1000, so no element
  // will repeat more than 1000 times. Therefore we can use another array to do
  // the counting sort over the occurrences.
  bool uniqueOccurrences_b(vector<int> &arr) {
    short m[2001] = {}, s[1001] = {};
    for (auto n : arr)
      ++m[n + 1000];
    for (auto i = 0; i < 2001; ++i)
      if (m[i] && ++s[m[i]] > 1)
        return false;
    return true;
  }

  bool uniqueOccurrences_2(vector<int> &arr) {
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

  // sol2's improve
  // https://leetcode.com/problems/contains-duplicate-ii/solutions/61599/C++-unordered_map-and-unordered_set/
  bool uniqueOccurrences_2b(vector<int> &arr) {
    unordered_map<int, int> freq;
    for (int num : arr) {
      freq[num]++;
    }

    unordered_set<int> freqSet;
    for (auto &p : freq)
      // The insert of unordered_set returns a pair with the second element
      // representing whether the element is actually inserted. to make the
      // thing clear: auto it = freqSet.insert(p.second);
      if (!freqSet.insert(p.second).second)
        return false;
    return true;
  }
};

int main() {
  Solution sol;
  std::vector<int> v1{1, 1, 2, 3, 3, 3};
  bool result = sol.uniqueOccurrences_b(v1);
  cout << result << endl;
  return 0;
};
