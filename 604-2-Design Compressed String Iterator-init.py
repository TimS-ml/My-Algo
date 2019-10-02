# https://leetcode-cn.com/problems/design-compressed-string-iterator/
# redundancy version

class StringIterator:
    def __init__(self, compressedString: str):
        self.string = compressedString
        self.len = len(compressedString)
        self.i = 0
        self.number = 0
        self.isfirst = True
        self.count = 0
        self.letter = ''

    def next(self) -> str:
        if self.i >= self.len:
            return ' '
        if self.count == 0:
            self.isfirst = True
        if self.isfirst == True:
            self.letter = self.string[self.i]
            self.number = self.string[self.i+1]
            self.count = int(self.number)
            self.isfirst = False
            self.i += 2
            self.count -= 1
        elif self.count > 0:  # e2
            self.count -= 1
        return self.letter

    def hasNext(self) -> bool:
        if self.i < self.len:
            return True
        return False


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()

compressedString = "L1e2t1C1o1d1e1"
compressedString2 = "L10e2t1C1o1d1e11"
obj = StringIterator(compressedString2)
for i in range(int(len(compressedString2)/2)+5):
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
