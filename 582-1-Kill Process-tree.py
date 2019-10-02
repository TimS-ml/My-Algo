# https://leetcode-cn.com/problems/kill-process/
# Unfinish...


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
    def killProcess(self, pid, ppid, kill):
        return

pid =  [1, 3, 10, 5]
ppid = [3, 0, 5, 3]
kill = 5
# print(Solution().killProcess(pid, ppid, kill))

n = len(pid)
mpppid = {}
for i in range(n):
    if ppid[i] in mpppid.keys():
        mpppid[ppid[i]].append(i)
    else:
        mpppid[ppid[i]] = [i]
# print(mpppid)
# {3: [0, 3], 0: [1], 5: [2]}

tree = Tree()
node = pid[ppid.index(0)]
tree.add(node)

for j in mpppid[node]:
    # print(j)
    tree.add(pid[j])

# tree.level_queue(tree.root)
