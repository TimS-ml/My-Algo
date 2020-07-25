'''
# Code Explain:
- Time complexity: O(log(n))
- Space complexity: O(log(n))

The most intuitive way for me is do this recursively

# Pros and Cons:
## Pros:

## Cons:

# Notation:

'''

class Solution:
    def addDigits(self, num: int) -> int:
        if num // 10 == 0:
            return num
        li = list(map(int, str(num)))
        # li = list(str(num))
        # li = [int(i) for i in li]
        num = sum(li)
        return self.addDigits(num)


# nums, target
IN = [
    (38), 
    (128), 
    (5)
]
useSet = 1
print(Solution().addDigits(IN[useSet]))

