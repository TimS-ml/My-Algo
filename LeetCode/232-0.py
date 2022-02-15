'''
# Code Explain:
- Time complexity: O()
- Space complexity: O()



- 栈是一种后进先出的数据结构
    - 元素从顶端入栈, 从顶端出栈
- 队列是一种先进先出的数据结构
    - 元素从后端入队, 从前端出队
'''


class MyQueue(object):
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x):
        self.input.append(x)

    def pop(self):
        self.peek()
        return self.output.pop()

    def peek(self):
        if (self.output == []):
            while (self.input != []):
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self):
        return self.input == [] and self.output == []
