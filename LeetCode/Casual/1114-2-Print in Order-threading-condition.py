# https://leetcode-cn.com/problems/print-in-order/
# https://leetcode.com/problems/print-in-order/solution/
# 启动wait_for来阻塞每个函数，直到指示self.t为目标值的时候才释放线程
# with是配合Condition方法常用的语法，主要是替代try语句的

import threading


class Foo:
    def __init__(self):
        self.c = threading.Condition()
        self.t = 0

    def first(self, printFirst: 'Callable[[], None]') -> None:
        self.res(0, printFirst)

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.res(1, printSecond)

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.res(2, printThird)

    def res(self, val: int, func: 'Callable[[], None]') -> None:
        with self.c:
            self.c.wait_for(lambda: val == self.t)  # 参数是函数对象，返回值是bool类型
            func()
            self.t += 1
            self.c.notify_all()
