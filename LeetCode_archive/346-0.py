'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()

'''

class MovingAverage:
    def __init__(self, size: int):
        self.preS = [0]
        self.sum = 0
        self.s = size

    def next(self, val: int) -> float:
        self.sum += val
        self.preS.append(self.sum)

        if len(self.preS) - 1 < self.s:
            return self.preS[-1] / (len(self.preS)-1)
        else:
            return (self.preS[-1] - self.preS[-self.s-1]) / self.s


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
