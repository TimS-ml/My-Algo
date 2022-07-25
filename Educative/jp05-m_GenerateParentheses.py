'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''

class ParenthesesString:
    def __init__(self, str, openCount, closeCount):
        self.str = str
        self.openCount = openCount
        self.closeCount = closeCount

def generate_valid_parentheses(num):
    def backtracking(subStr, l, r):
        if len(subStr) == 2 * num:
            ans.append(subStr)
            return

        if l < num:
            backtracking(subStr + '(', l + 1, r)
        if l > r:
            backtracking(subStr + ')', l, r + 1)

    ans = []
    backtracking('', 0, 0)
    return ans



def main():
    print("All combinations of balanced parentheses are: " +
          str(generate_valid_parentheses(2)))
    print("All combinations of balanced parentheses are: " +
          str(generate_valid_parentheses(3)))


main()
