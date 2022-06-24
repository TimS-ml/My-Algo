'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

why two pointers ???
'''


def backspace_compare(str1, str2):
    def strClean(s):
        stack = []
        for c in s:
            if c == '#':
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)

    return strClean(str1) == strClean(str2)


def main():
    print(backspace_compare("xy#z", "xzz#"))
    print(backspace_compare("xy#z", "xyz#"))
    print(backspace_compare("xp#", "xyz##"))
    print(backspace_compare("xywrrmp", "xywrrmu#p"))


main()
