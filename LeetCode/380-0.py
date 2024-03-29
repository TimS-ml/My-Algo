'''
# Code Explain:
- Time complexity: O(1)
- Space complexity: O(N)

Starting from the Insert, we immediately have two good candidates with O(1):
- Hash (has problem with getRandom)
- Array List (has problem with delete)

[python - Set.pop() isn't random? - Stack Overflow](https://stackoverflow.com/questions/21017188/set-pop-isnt-random)
'''

from random import choice

class RandomizedSet():
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}  # value: idx dict
        self.list = []


    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.dict:
            return False

        # aims to locate the idx of this value in list
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True


    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.dict:
            # move the last element to the place idx of the element to delete
            last_element = self.list[-1]
            val_idx_to_del = self.dict[val]
            self.list[val_idx_to_del], self.dict[last_element] = last_element, val_idx_to_del

            # delete the last element
            self.list.pop()
            del self.dict[val]  # or self.dict.pop(val)
            return True

        return False


    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
