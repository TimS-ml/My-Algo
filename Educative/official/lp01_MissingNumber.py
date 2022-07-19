'''
Find Missing Number

# Code Explain:
- Time complexity: O()
- Space complexity: O()

A straight forward approach to solve this problem can be:
    Find the sum of all integers from 1 to n; let’s call it s1.
    Subtract all the numbers in the input array from s1; this will give us the missing number.
    While finding the sum of numbers from 1 to n, we can get integer overflow when n is large.
time: O(n)

'''


def find_missing_number_w(arr):
    L = len(arr) + 1
    # find sum of all numbers from 1 to n.
    s1 = 0
    for i in range(1, L + 1):
        s1 += i

    # subtract all numbers in input from sum.
    for n in arr:
        s1 -= n

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
    print('Missing number is:' + str(find_missing_number_w(arr)))
    print('Missing number is:' + str(find_missing_number(arr)))


main()


'''
Find Single Number

# Code Explain:
- Time complexity: O()
- Space complexity: O()

One straight forward solution can be to use a HashMap kind of data structure and iterate through the input:
    If number is already present in HashMap, remove it.
    If number is not present in HashMap, add it.
    In the end, only number left in the HashMap is our required single number.
Time and space complexity Time Complexity of the above solution will be O(n)
 and space complexity will also be O(n)
'''


def find_single_number(arr):
    num = 0
    for i in arr:
        num ^= i
    return num


def main_2():
    arr = [1, 4, 2, 1, 3, 2, 3]
    print(find_single_number(arr))


main_2()
