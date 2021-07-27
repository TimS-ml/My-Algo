'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

# Pros and Cons and Notation:

self.p  : (position) Save the next character to be generated in cstr
self.num: Number of char left
'''

import re


class StringIterator:
    def __init__(self, compressedString: str):
        self.cstr = compressedString
        self.size = len(compressedString)
        self.num = 0  # since num=0, first .next() will update everything
        self.p = 0
        self.char = ''

    def next(self) -> str:
        if not self.hasNext(): return ' '

        if self.num == 0:
            self.char = self.cstr[self.p]
            self.p += 1  # move to number
            # in case that is > 1 dig number
            while self.p < self.size and self.cstr[self.p] in '0123456789':
                self.num = self.num * 10 + int(self.cstr[self.p])
                self.p += 1
            # now the self.num and self.char, self.p all updated

        self.num -= 1
        return self.char

    def hasNext(self) -> bool:
        return self.p != self.size or self.num != 0


class StringIterator_mod:
    def __init__(self, compressedString: str):
        self.char_li = re.split('[0-9]+', compressedString)
        self.num_li = [
            int(n) for n in re.split('[a-zA-z]+', compressedString)[1:]
        ]
        self.size = len(self.char_li) - 1
        self.p = 0

    def next(self) -> str:
        if not self.hasNext(): return ' '

        self.num_li[self.p] -= 1
        ans = self.char_li[self.p]
        if self.num_li[self.p] == 0:
            self.p += 1
        return ans

    def hasNext(self) -> bool:
        return self.p != self.size


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()

# compressedString = "L1e2t1C1o1d1e1"
compressedString = "L10e2t1C1o1d1e11"
obj = StringIterator(compressedString)
for i in range(int(len(compressedString) / 2) + 5):
    print(obj.next())
    print(obj.hasNext())

# param_1 = obj.next()
# param_2 = obj.hasNext()
# obj.next()  # return 'L'
# obj.next()  # return 'e'
# obj.next()  # return 'e'
# obj.next()  # return 't'
# obj.next()  # return 'C'
# obj.next()  # return 'o'
# obj.next()  # return 'd'
# obj.hasNext()  # return true
# obj.next()  # return 'e'
# obj.hasNext()  # return false
# obj.next()  # return ' '
