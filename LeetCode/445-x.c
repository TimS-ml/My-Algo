#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Definition for singly-linked list.
struct ListNode {
    int val;
    struct ListNode *next;
};

// Stack implementation
struct Stack {
    int top;
    unsigned capacity;
    int* array;
};

// Function prototypes
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2);
struct Stack* createStack(unsigned capacity);
void push(struct Stack* stack, int item);
int pop(struct Stack* stack);
int isEmpty(struct Stack* stack);
struct ListNode* createNode(int val);
struct ListNode* createLinkedList(int* nums, int size);
int* linkedListToArray(struct ListNode* head, int* size);

// Main solution function
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct Stack* s1 = createStack(1000);  // Assume max 1000 elements
    struct Stack* s2 = createStack(1000);
    
    // Push values from linked lists onto stacks
    while (l1) {
        push(s1, l1->val);
        l1 = l1->next;
    }
    while (l2) {
        push(s2, l2->val);
        l2 = l2->next;
    }
    
    struct ListNode* result = NULL;
    int carry = 0;
    
    while (!isEmpty(s1) || !isEmpty(s2) || carry) {
        int sum = carry;
        
        if (!isEmpty(s1)) {
            sum += pop(s1);
        }
        if (!isEmpty(s2)) {
            sum += pop(s2);
        }
        
        struct ListNode* newNode = createNode(sum % 10);
        newNode->next = result;
        result = newNode;
        
        carry = sum / 10;
    }
    
    free(s1->array);
    free(s1);
    free(s2->array);
    free(s2);
    
    return result;
}

// Stack functions
struct Stack* createStack(unsigned capacity) {
    struct Stack* stack = (struct Stack*)malloc(sizeof(struct Stack));
    stack->capacity = capacity;
    stack->top = -1;
    stack->array = (int*)malloc(stack->capacity * sizeof(int));
    return stack;
}

void push(struct Stack* stack, int item) {
    stack->array[++stack->top] = item;
}

int pop(struct Stack* stack) {
    return stack->array[stack->top--];
}

int isEmpty(struct Stack* stack) {
    return stack->top == -1;
}

// Helper functions
struct ListNode* createNode(int val) {
    struct ListNode* newNode = (struct ListNode*)malloc(sizeof(struct ListNode));
    newNode->val = val;
    newNode->next = NULL;
    return newNode;
}

struct ListNode* createLinkedList(int* nums, int size) {
    struct ListNode dummy = {0, NULL};
    struct ListNode* current = &dummy;
    for (int i = 0; i < size; i++) {
        current->next = createNode(nums[i]);
        current = current->next;
    }
    return dummy.next;
}

int* linkedListToArray(struct ListNode* head, int* size) {
    int* result = NULL;
    int capacity = 10;
    *size = 0;
    result = (int*)malloc(capacity * sizeof(int));
    
    while (head) {
        if (*size >= capacity) {
            capacity *= 2;
            result = (int*)realloc(result, capacity * sizeof(int));
        }
        result[(*size)++] = head->val;
        head = head->next;
    }
    
    return result;
}

int main() {
    FILE* infile = fopen("445.txt", "r");
    if (infile == NULL) {
        printf("Error opening file\n");
        return 1;
    }

    char line[1000];
    int testCase = 1;

    while (fgets(line, sizeof(line), infile)) {
        // Read first linked list
        int nums1[1000], size1 = 0;
        char* token = strtok(line, " \n");
        while (token != NULL) {
            nums1[size1++] = atoi(token);
            token = strtok(NULL, " \n");
        }

        // Read second linked list
        fgets(line, sizeof(line), infile);
        int nums2[1000], size2 = 0;
        token = strtok(line, " \n");
        while (token != NULL) {
            nums2[size2++] = atoi(token);
            token = strtok(NULL, " \n");
        }

        // Read expected result
        fgets(line, sizeof(line), infile);
        int expected[1000], sizeExpected = 0;
        token = strtok(line, " \n");
        while (token != NULL) {
            expected[sizeExpected++] = atoi(token);
            token = strtok(NULL, " \n");
        }

        // Create linked lists
        struct ListNode* l1 = createLinkedList(nums1, size1);
        struct ListNode* l2 = createLinkedList(nums2, size2);

        // Solve and get result
        struct ListNode* result = addTwoNumbers(l1, l2);
        int sizeResult;
        int* resultArray = linkedListToArray(result, &sizeResult);

        // Print test case results
        printf("Test Case %d:\n", testCase);
        printf("Input: l1 = ");
        for (int i = 0; i < size1; i++) printf("%d ", nums1[i]);
        printf(", l2 = ");
        for (int i = 0; i < size2; i++) printf("%d ", nums2[i]);
        printf("\nOutput: ");
        for (int i = 0; i < sizeResult; i++) printf("%d ", resultArray[i]);
        printf("\nExpected: ");
        for (int i = 0; i < sizeExpected; i++) printf("%d ", expected[i]);
        printf("\nResult: %s\n\n", (sizeResult == sizeExpected && memcmp(resultArray, expected, sizeExpected * sizeof(int)) == 0) ? "Correct" : "Wrong");

        // Free memory
        free(resultArray);
        while (l1) {
            struct ListNode* temp = l1;
            l1 = l1->next;
            free(temp);
        }
        while (l2) {
            struct ListNode* temp = l2;
            l2 = l2->next;
            free(temp);
        }
        while (result) {
            struct ListNode* temp = result;
            result = result->next;
            free(temp);
        }

        testCase++;
    }

    fclose(infile);
    return 0;
}
