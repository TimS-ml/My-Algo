# https://leetcode-cn.com/problems/implement-stack-using-queues/
# stack:  last in - first out， LIFO
#   if push 1, 2, then pop -> return 2
# queues: first in - first out，FIFO

from collections import deque


class MyStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = deque()
        self.help = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        while len(self.queue) > 1:
            self.help.append(self.queue.popleft())
        tmp = self.queue.popleft()
        self.help, self.queue = self.queue, self.help
        return tmp

    def top(self) -> int:
        """
        Get the top element.
        """
        while len(self.queue) != 1:
            self.help.append(self.queue.popleft())
        tmp = self.queue.popleft()
        self.help.append(tmp)
        self.help, self.queue = self.queue, self.help
        return tmp

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not bool(self.queue)


stack = MyStack()
print(stack.push(1))
print(stack.push(2)) 
print(stack.push(3)) 
print(stack.top())
print(stack.pop())
print(stack.empty())

