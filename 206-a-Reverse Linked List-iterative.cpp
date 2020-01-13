# include <iostream>
# include <vector>
using namespace std;



// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};


class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        // just like solution 1, but in solution 1
        // curr = head, and we use curr.next (based on python Linked List structure)
        // prev is the new head
        ListNode *prev = NULL, *nextTemp=NULL;
        while (head){
            nextTemp = head->next;
            head->next = prev;
            prev = head;
            head = nextTemp;
        }
        return prev;
    }
};

