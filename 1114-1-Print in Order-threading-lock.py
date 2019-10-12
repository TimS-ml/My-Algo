# https://leetcode-cn.com/problems/print-in-order/
# https://leetcode.com/problems/print-in-order/solution/
# 类初始化的时候不能包含有参数，所以要写一句acquire进行阻塞，调用其他函数的时候按顺序release释放


from threading import Lock


class Foo:
    def __init__(self):
        self.firstJobDone = Lock()
        self.secondJobDone = Lock()
        self.firstJobDone.acquire()
        self.secondJobDone.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first".
        printFirst()
        # Notify the thread that is waiting for the first job to be done.
        self.firstJobDone.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        # Wait for the first job to be done
        with self.firstJobDone:
            # printSecond() outputs "second".
            printSecond()
            # Notify the thread that is waiting for the second job to be done.
            self.secondJobDone.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        # Wait for the second job to be done.
        with self.secondJobDone:
            # printThird() outputs "third".
            printThird()
