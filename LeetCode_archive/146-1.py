'''
# Code Explain:
- Time complexity: O(1)
- Space complexity: O(capacity)

'''

class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = dict()
        # Dummy head and tail
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # if key in self.cache
        # locate(dict) then move to head(DLinkedNode)
        node = self.cache[key]
        self.moveToHead(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            # update dict and head of DLinkedNode
            node = DLinkedNode(key, value)
            self.cache[key] = node
            self.addToHead(node)
            self.size += 1

            # remove tail's node if exceed capacity
            if self.size > self.capacity:
                removed = self.removeTail()
                # remember to update dict
                self.cache.pop(removed.key)
                self.size -= 1
        else:
            # if key exsit
            # [1] locate using dict
            # [2] update value
            # [3] move to DLinkedNode's head
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)

    def addToHead(self, node):
        # add node after head
        node.prev = self.head
        node.next = self.head.next
        # (head.next).prev and (head).next
        self.head.next.prev = node
        self.head.next = node

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)

    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node
