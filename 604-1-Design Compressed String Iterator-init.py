# https://leetcode-cn.com/problems/design-compressed-string-iterator/


class StringIterator:
    def __init__(self, compressedString):
        self.data = compressedString
        self.idx = -1
        self.decodeNext()

    # find the end edge
    def decodeNext(self):
        self.idx += 1
        if self.idx + 1 < len(self.data):
            self.cur = self.data[self.idx]
            end = self.idx + 1
            while end < len(self.data) and self.data[end].isdigit():
                end += 1
            # print(end)
            self.num = int(self.data[self.idx+1:end])
            self.idx = end - 1

    def next(self):
        if self.hasNext():
            ret = self.cur
            self.num -= 1
            if self.num <= 0:
                self.decodeNext()
            return ret
        return " "

    def hasNext(self):
        return self.idx < len(self.data) and self.num > 0


compressedString1 = "L1e2t1C1o1d1e1"
compressedString2 = "L10e2t1C1o1d1e11"
obj = StringIterator(compressedString1)
for i in range(int(len(compressedString1)/2)+5):
    print(obj.next())
    # print(obj.hasNext())
