#include <iostream>
#include <unordered_map>
#include <vector>
#include <fstream>
#include <sstream>
#include <functional>
#include <stack>
// using std::unordered_map;
// using std::vector;
using namespace std;

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        stack<int> s1, s2;
        
        // Push values from linked lists onto stacks
        while (l1) {
            s1.push(l1->val);
            l1 = l1->next;
        }
        while (l2) {
            s2.push(l2->val);
            l2 = l2->next;
        }
        
        ListNode* result = nullptr;
        int carry = 0;
        
        while (!s1.empty() || !s2.empty() || carry) {
            int sum = carry;
            
            if (!s1.empty()) {
                sum += s1.top();
                s1.pop();
            }
            if (!s2.empty()) {
                sum += s2.top();
                s2.pop();
            }
            
            ListNode* newNode = new ListNode(sum % 10);
            newNode->next = result;
            result = newNode;
            
            carry = sum / 10;
        }
        
        return result;
    }
};

// Helper function to create a linked list from a vector
ListNode* createLinkedList(const vector<int>& nums) {
    ListNode dummy(0);
    ListNode* current = &dummy;
    for (int num : nums) {
        current->next = new ListNode(num);
        current = current->next;
    }
    return dummy.next;
}

// Helper function to convert a linked list to a vector
vector<int> linkedListToVector(ListNode* head) {
    vector<int> result;
    while (head) {
        result.push_back(head->val);
        head = head->next;
    }
    return result;
}

using SolutionFunc = function<ListNode*(ListNode*, ListNode*)>;

SolutionFunc currentSolution;

int main() {
    Solution sol;
    currentSolution = bind(&Solution::addTwoNumbers, &sol, placeholders::_1, placeholders::_2);

    ifstream infile("445.txt");
    string line;
    int testCase = 1;

    while (getline(infile, line)) {
        // Read first linked list
        vector<int> nums1;
        istringstream iss1(line);
        int num;
        while (iss1 >> num) {
            nums1.push_back(num);
        }

        // Read second linked list
        getline(infile, line);
        vector<int> nums2;
        istringstream iss2(line);
        while (iss2 >> num) {
            nums2.push_back(num);
        }

        // Read expected result
        getline(infile, line);
        vector<int> expected;
        istringstream iss3(line);
        while (iss3 >> num) {
            expected.push_back(num);
        }

        // Create linked lists
        ListNode* l1 = createLinkedList(nums1);
        ListNode* l2 = createLinkedList(nums2);

        // Solve and get result
        ListNode* result = currentSolution(l1, l2);
        vector<int> resultVec = linkedListToVector(result);

        // Print test case results
        cout << "Test Case " << testCase << ":" << endl;
        cout << "Input: l1 = ";
        for (int n : nums1) cout << n << " ";
        cout << ", l2 = ";
        for (int n : nums2) cout << n << " ";
        cout << endl;
        cout << "Output: ";
        for (int n : resultVec) cout << n << " ";
        cout << endl;
        cout << "Expected: ";
        for (int n : expected) cout << n << " ";
        cout << endl;
        cout << "Result: " << (resultVec == expected ? "Correct" : "Wrong") << endl;
        cout << endl;

        testCase++;
    }

    return 0;
}
