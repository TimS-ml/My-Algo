# Links
https://leetcode.com/problems/kth-largest-element-in-an-array/
https://leetcode.com/problems/kth-largest-element-in-an-array/discuss/
https://leetcode.com/problems/kth-largest-element-in-an-array/discuss/60306/Python-different-solutions-with-comments-(bubble-sort-selection-sort-heap-sort-and-quick-sort).

l book p137
https://books.halfrost.com/leetcode/ChapterFour/0200~0299/0215.Kth-Largest-Element-in-an-Array/


# Thought Process
This is slow, O(N logN)
We can reduce this to O(N logK)

```python
def findKthLargest(self, nums: List[int], k: int) -> int:
    nums.sort(reverse=True)
    # print(nums)
    return nums[k - 1]
```

# Test Cases

