# A straight forward approach to solve this problem can be:
# Find the sum of all integers from 11 to nn; let’s call it s1.
# Subtract all the numbers in the input array from s1; this will give us the missing number.
# While finding the sum of numbers from 1 to nn, we can get integer overflow when nn is large.
# time: O(n)


def find_missing_number_w(arr):
    n = len(arr) + 1
    # find sum of all numbers from 1 to n.
    s1 = 0
    for i in range(1, n + 1):
        s1 += i

    # subtract all numbers in input from sum.
    for i in arr:
        s1 -= i

    # s1, now, is the missing number
    return s1


# Remember the important property of XOR that it returns 0 if both the bits in comparison are the same.
def find_missing_number(arr):
    n = len(arr) + 1
    # x1 represents XOR of all values from 1 to n
    x1 = 1
    for i in range(2, n + 1):
        x1 = x1 ^ i

    # x2 represents XOR of all values in arr
    x2 = arr[0]
    for i in range(1, n - 1):
        x2 = x2 ^ arr[i]

    print('{0:b}'.format(x1), '{0:b}'.format(x2))
    # missing number is the xor of x1 and x2
    return x1 ^ x2


def main():
    arr = [1, 5, 2, 6, 4]
    print('Missing number is:' + str(find_missing_number(arr)))


main()
