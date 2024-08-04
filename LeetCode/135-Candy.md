# Links
https://leetcode.com/problems/candy/description/


# Thought Process
neighbor = compare x with x-1 and x+1
left to right: if x > x-1, x = x-1 + 1
right to left: if x > x+1, x = x+1 + 1
Plus, check if you really need to update the value of x, if x is already greater than x-1 or x+1, then no need to update x.

NOTE: keep in mind that the left to right and right to left are independent of each other!!!


# Test Cases

