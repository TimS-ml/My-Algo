'''
# Code Explain:
- Time complexity: O(N * 2^N)
- Space complexity: O(N * 2^N)

lc 22
'''

from collections import deque


class ParenthesesString:
    def __init__(self, str, openCount, closeCount):
        self.str = str
        self.openCount = openCount
        self.closeCount = closeCount


def generate_valid_parentheses(num):
    result = []
    queue = deque()
    queue.append(ParenthesesString("", 0, 0))
    while queue:
        ps = queue.popleft()
        # if we've reached the maximum number of open and close parentheses, add to the result
        if ps.openCount == num and ps.closeCount == num:
            result.append(ps.str)
        else:
            if ps.openCount < num:  # if we can add an open parentheses, add it
                queue.append(
                    ParenthesesString(ps.str + "(", ps.openCount + 1,
                                      ps.closeCount))

            if ps.openCount > ps.closeCount:  # if we can add a close parentheses, add it
                queue.append(
                    ParenthesesString(ps.str + ")", ps.openCount,
                                      ps.closeCount + 1))

    return result


def main():
    print("All combinations of balanced parentheses are: " +
          str(generate_valid_parentheses(2)))
    print("All combinations of balanced parentheses are: " +
          str(generate_valid_parentheses(3)))


main()
