'''
Any number will be called a happy number if, after repeatedly replacing it with a number equal to the sum of the square of all of its digits, leads us to number '1'.
All other (not-happy) numbers will never reach '1'. Instead, they will be stuck in a cycle of numbers which does not include '1'.

# Code Explain:
- Time complexity: O(longN)
- Space complexity: O(1)

lc 202
this is not a link list problem but same

Each number will definitely have a cycle.
https://en.wikipedia.org/wiki/Happy_number
'''


def find_happy_number(num):
    slow, fast = num, num
    while True:
        slow = find_square_sum(slow)  # move one step
        fast = find_square_sum(find_square_sum(fast))  # move two steps
        if slow == fast:  # found the cycle
            break
    return slow == 1  # see if the cycle is stuck on the number '1'


def find_square_sum(num):
    _sum = 0
    while (num > 0):
        digit = num % 10
        _sum += digit * digit
        num //= 10
    return _sum


def main():
    print(find_happy_number(23))
    print(find_happy_number(12))


main()
