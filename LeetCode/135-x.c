#include <stdio.h>
#include <stdlib.h>

int candy(int* ratings, int ratingsSize) {
    if (ratingsSize < 2) return ratingsSize;  // corner case, one kid

    int* num = (int*)malloc(ratingsSize * sizeof(int));
    if (num == NULL) {
        // Handle memory allocation failure
        return 0;
    }

    // Initialize with 1 candy for each kid
    for (int i = 0; i < ratingsSize; i++) {
        num[i] = 1;
    }
    
    // left to right
    for (int i = 1; i < ratingsSize; ++i) {
        if (ratings[i] > ratings[i - 1]) {
            num[i] = num[i - 1] + 1;
        }
    }

    // right to left
    for (int i = ratingsSize - 1; i > 0; --i) {
        if (ratings[i - 1] > ratings[i]) {
            num[i - 1] = (num[i - 1] > num[i] + 1) ? num[i - 1] : (num[i] + 1);
        }
    }

    // Sum up the candies
    int total = 0;
    for (int i = 0; i < ratingsSize; i++) {
        total += num[i];
    }

    free(num);  // Don't forget to free the allocated memory
    return total;
}

int main() {
    FILE* file = fopen("135.txt", "r");
    if (file == NULL) {
        printf("Error opening file\n");
        return 1;
    }

    int testCase = 1;
    int ratings[10000];  // Assuming maximum input size
    int ratingsSize = 0;
    int expectedAnswer;

    while (fscanf(file, "%d", &ratings[ratingsSize]) == 1) {
        ratingsSize++;
        if (fgetc(file) == '\n') {
            fscanf(file, "%d", &expectedAnswer);
            
            int result = candy(ratings, ratingsSize);
            printf("Test Case %d: %d, %s\n", testCase, result, 
                   (result == expectedAnswer ? "Correct" : "Wrong"));
            
            testCase++;
            ratingsSize = 0;
        }
    }

    fclose(file);
    return 0;
}
