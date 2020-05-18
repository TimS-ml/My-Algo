# https://leetcode-cn.com/problems/implement-stack-using-queues/
# stack:  last in - first out， LIFO
#   if push 1, 2, then pop -> return 2
# queues: first in - first out，FIFO
# this is non-queues approach, don't do that...


class MyStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.queue.pop()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queue[-1]


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

