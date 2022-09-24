'''
# Code Explain:

sol 1: heap
- Time complexity: O(min(K, N) + KlogN)
- Space complexity: O(N)

sol 2: binary search
- Time complexity: O(log(max-min))
- Space complexity: O(1)

lc 378
'''


def find_Kth_smallest(matrix, k):
    minHeap = []

    # put the 1st element of each row in the min heap
    # we don't need to push more than 'k' elements in the heap
    for i in range(min(k, len(matrix))):
        heappush(minHeap, (matrix[i][0], 0, matrix[i]))

    # take the smallest(top) element form the min heap, if the running count is equal to k' return the number
    # if the row of the top element has more elements, add the next element to the heap
    numberCount, number = 0, 0
    while minHeap:
        number, i, row = heappop(minHeap)
        numberCount += 1
        if numberCount == k:
            break
        if len(row) > i + 1:
            heappush(minHeap, (row[i + 1], i + 1, row))
    return number


# binary search
def find_Kth_smallest_2(matrix, k):
    n = len(matrix)
    start, end = matrix[0][0], matrix[n - 1][n - 1]
    while start < end:
        mid = start + (end - start) / 2
        smaller, larger = (matrix[0][0], matrix[n - 1][n - 1])

        count, smaller, larger = count_less_equal(matrix, mid, smaller, larger)

        if count == k:
            return smaller
        if count < k:
            start = larger  # search higher
        else:
            end = smaller  # search lower

    return start


def count_less_equal(matrix, mid, smaller, larger):
    count, n = 0, len(matrix)
    row, col = n - 1, 0
    while row >= 0 and col < n:
        if matrix[row][col] > mid:
            # as matrix[row][col] is bigger than the mid, let's keep track of the
            # smallest number greater than the mid
            larger = min(larger, matrix[row][col])
            row -= 1
        else:
            # as matrix[row][col] is less than or equal to the mid, let's keep track of the
            # biggest number less than or equal to the mid
            smaller = max(smaller, matrix[row][col])
            count += row + 1
            col += 1

    return count, smaller, larger


def main():
    print("Kth smallest number is: " +
          str(find_Kth_smallest([[1, 4], [2, 5]], 2)))

    print("Kth smallest number is: " + str(find_Kth_smallest([[-5]], 1)))

    print("Kth smallest number is: " +
          str(find_Kth_smallest([[2, 6, 8], [3, 7, 10], [5, 8, 11]], 5)))

    print("Kth smallest number is: " +
          str(find_Kth_smallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8)))


main()
