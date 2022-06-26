'''
Any number will be called a happy number if, after repeatedly replacing it with a number equal to the sum of the square of all of its digits, leads us to number ‘1’. 
All other (not-happy) numbers will never reach ‘1’. Instead, they will be stuck in a cycle of numbers which does not include ‘1’.

# Code Explain:
- Time complexity: O(longN)
- Space complexity: O(1)


Each number will definitely have a cycle.
https://en.wikipedia.org/wiki/Happy_number
'''


def find_happy_number(n):
    def get_next(n):
        total_sum = 0
        while n > 0:
            n, digit = divmod(n, 10)
            total_sum += digit**2
        return total_sum

    slow = n
    fast = get_next(n)
    while slow != fast:
        slow = get_next(slow)
        fast = get_next(get_next(fast))
    return slow == 1


def main():
    print(find_happy_number(23))
    print(find_happy_number(12))


main()
