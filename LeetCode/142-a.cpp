/*
# Code Explain:
- Time complexity: O()
- Space complexity: O()

*/

#include <fstream>
#include <functional>
#include <iostream>
#include <vector>
using namespace std;

// Definition for singly-linked list.
struct ListNode {
  int val;
  ListNode *next;
  ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
public:
  ListNode *detectCycle(ListNode *head) { 
    ListNode *slow = head, *fast = head;
    do {
      if (!fast || !fast->next) return nullptr;
      fast = fast->next->next;
      slow = slow->next;
    } while (fast != slow);
    fast = head;
    while (fast != slow){
      slow = slow->next;
      fast = fast->next;
    }
    return fast;
  }
};

using SolutionFunc = function<ListNode *(ListNode *)>;

SolutionFunc currentSolution;

int main() {
  Solution sol;
  currentSolution = bind(&Solution::detectCycle, &sol, placeholders::_1);

  ifstream inputFile("142.txt");

  if (!inputFile.is_open()) {
    cout << "Error opening file" << endl;
    return 1;
  }

  int testCase = 1;
  int n;

  while (inputFile >> n) {
    if (n == 0)
      break; // End of file

    // Read node values
    vector<int> values(n);
    for (int i = 0; i < n; i++) {
      inputFile >> values[i];
    }

    // Read cycle position
    int pos;
    inputFile >> pos;

    // Create linked list
    vector<ListNode *> nodes;
    for (int val : values) {
      nodes.push_back(new ListNode(val));
    }

    for (int i = 0; i < n - 1; i++) {
      nodes[i]->next = nodes[i + 1];
    }

    // Create cycle if pos != -1
    if (pos != -1 && pos < n) {
      nodes[n - 1]->next = nodes[pos];
    }

    // Expected output is the index of the node where cycle begins
    int expected_pos = pos;

    // Run the solution
    ListNode *result = currentSolution(n > 0 ? nodes[0] : nullptr);

    // Find the position of the result node
    int result_pos = -1;
    if (result != nullptr) {
      for (int i = 0; i < nodes.size(); i++) {
        if (nodes[i] == result) {
          result_pos = i;
          break;
        }
      }
    }

    cout << "Test Case " << testCase << ": " << result_pos << ", "
         << (result_pos == expected_pos ? "Correct" : "Wrong") << endl;

    testCase++;

    // Clean up memory
    if (pos == -1) {
      // No cycle, can delete all nodes
      for (auto node : nodes) {
        delete node;
      }
    } else {
      // Has cycle, break it first
      if (n > 0)
        nodes[n - 1]->next = nullptr;
      for (auto node : nodes) {
        delete node;
      }
    }
  }

  inputFile.close();
  return 0;
}
