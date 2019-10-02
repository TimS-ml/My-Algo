# https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree/


# 相当于整个ListNode都存储在head里
class ListNode:
    def __init__(self, x, next = None):
        self.val = x
        self.next = next
    def __repr__(self):  # 只返回当前node的数值……循环添加节点的时候有些用
        return str(self.val)  # 否则TypeError: __str__ returned non-string (type int)


class TreeNode(object):
    def __init__(self, val=-1, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


class Tree(object):
    def __init__(self):
        self.root = TreeNode()
        self.myQueue = []

    def add(self, val):
        node = TreeNode(val)
        
        # 如果树是空的，则对根节点赋值
        if self.root.val == -1:
            self.root = node
            self.myQueue.append(self.root)
            print(self.myQueue, self.root.val, 'top')
        
        # 如果有根节点
        else:
            treeNode = self.myQueue[0]  # 检查myQueue[0]的子树
            if treeNode.left == None:
                treeNode.left = node
                self.myQueue.append(treeNode.left)
                print(self.myQueue, self.root.val, 'left')
            else:
                treeNode.right = node
                self.myQueue.append(treeNode.right)
                self.myQueue.pop(0)  # myQueue[0]节点左右都有了，pop掉
                print(self.myQueue, self.root.val, 'right')

    def level_queue(self, root):
        if root == None:
            return
        myQueue = []
        node = root
        myQueue.append(node)
        while myQueue:
            node = myQueue.pop(0)
            print(node.val)
            if node.left != None:
                myQueue.append(node.left)
            if node.right != None:
                myQueue.append(node.right)


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if head:
            pre = None
            slow = fast = head
            while fast and fast.next:
                pre = slow
                slow = slow.next
                fast = fast.next.next
            root = TreeNode(slow.val)
            if pre:
                pre.next = None
                root.left = self.sortedListToBST(head)
            root.right = self.sortedListToBST(slow.next)
            return root


vals1 = [-10, -3, 0, 5, 9]
# tree = Tree()

# for i in range(len(vals1)):
#     tree.add(vals1[i])

# tree.level_queue(tree.root)

head = None
head_list = reversed(vals1)  # 最后输入的是9，所以是第一个元素
for count in range(len(head_list)):
    head = ListNode(head_list[count], head)
    print(head)

# print(head)

while head:
    print(head.val)
    head = head.next

print(Solution().isBalanced(tree.root))
