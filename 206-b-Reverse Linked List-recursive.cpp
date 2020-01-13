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
        if (head==NULL || head->next==NULL)
            return head;
        ListNode *curr = reverseList(head->next);
        // If Linked List is 1->2->3->4->5
        // Then 4->5->NULL
        // curr is 5, head is 4
        // head.next.next is NULL, head.next is 5
        // So head.next.next is 5->4 (head.next is 5)
        // After that, 3->4->NULL and 5->4, recursive
        head->next->next = head;
        head->next = NULL;
        return curr;
    }
};

