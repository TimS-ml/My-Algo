'''
# Code Explain:
- Time complexity: O(1)
- Space complexity: O(capacity)

'''

from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.dic = OrderedDict()
        self.c = capacity
    
    def get(self, key):
        if key not in self.dic:
            return -1
        v = self.dic.pop(key) 
        self.dic[key] = v  # set key as the newest one
        return v
    
    def put(self, key, value):
        if key in self.dic:    
            self.dic.pop(key)
        else:
            if self.c > 0:
                self.c -= 1  
            else:  # self.dic is full
                self.dic.popitem(last=False) 
        self.dic[key] = value


# This is build on top of OrderedDict
class LRUCache_2(OrderedDict):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.c = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self:
            return - 1
        
        self.move_to_end(key)
        return self[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.c:
            self.popitem(last = False)


