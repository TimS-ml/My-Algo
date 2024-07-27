#include <stdio.h>
#include <stdlib.h>

// Comparison function for qsort
int compare(const void* a, const void* b) {
    return (*(int*)a - *(int*)b);
}

int findContentChildren(int* g, int gSize, int* s, int sSize) {
    // Sort children's greed factors and cookie sizes
    qsort(g, gSize, sizeof(int), compare);
    qsort(s, sSize, sizeof(int), compare);

    int i = 0, j = 0;
    while (i < gSize && j < sSize) {
        // If the current cookie can satisfy the current child
        if (g[i] <= s[j]) {
            i++;  // Move to the next child
        }
        j++;  // Always try the next cookie, regardless of satisfaction
    }

    return i;  // Return the number of satisfied children
}

int main() {
    FILE* file = fopen("455.txt", "r");
    if (file == NULL) {
        printf("Error opening file\n");
        return 1;
    }

    int testCase = 1;
    int g[1000], s[1000];  // Assume maximum input size of 1000
    int gSize, sSize;
    int expectedAnswer;

    while (1) {
        // Read children's greed factors
        gSize = 0;
        while (fscanf(file, "%d", &g[gSize]) == 1) {
            gSize++;
            if (fgetc(file) == '\n') break;
        }

        if (gSize == 0) break;  // End of file

        // Read cookie sizes
        sSize = 0;
        while (fscanf(file, "%d", &s[sSize]) == 1) {
            sSize++;
            if (fgetc(file) == '\n') break;
        }

        // Read expected answer
        fscanf(file, "%d", &expectedAnswer);

        // Call function and output result
        int result = findContentChildren(g, gSize, s, sSize);
        printf("Test Case %d: %d, %s\n", testCase, result, 
               (result == expectedAnswer ? "Correct" : "Wrong"));

        testCase++;
    }

    fclose(file);
    return 0;
}
