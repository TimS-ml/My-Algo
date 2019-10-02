# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(-1)  # 哑结点，在头部，以应对极端情况
        dummy.next = head
        tmp = dummy
        lenth = 0

        # 计算ListNode的长度
        while tmp:  
            tmp = tmp.next
            lenth += 1
        # print('lenth', lenth)

        # 修改ListNode，边界问题需要注意
        # 如果count = lenth - n，则一开始进while就会向前推一步，整好是要删除的节点的位置
        tmp = dummy
        count = lenth - n - 1
        print('count', count)
        while count:
            tmp = tmp.next
            count -= 1
            print(tmp, count)  # 最后是3 0

        tmp.next = tmp.next.next
        return dummy.next

## input是存储在json里的
def stringToIntegerList(input):
    return json.loads(input)

def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr

def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            head = stringToListNode(line);
            line = next(lines)
            n = int(line);
            
            ret = Solution().removeNthFromEnd(head, n)

            out = listNodeToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
