Only the python solution contains the time complexity stuffs
For problem set:
- write down thought process first
  - update which part stacked
- this problem is similar to which example problems


# Sliding Window
2 pointers, fixed / unfixed gap

state related: hash dict

string + parameters

fix size, find max sum sub arr
fix sum, find shortest size sub arr
fix `<= k` distinct character, find longest size sub arr
allow distinct character, no repeat, find longest size sub arr


## Key
fixed size or dynamic size ?
  - relationship to the parameters ? How to def start and end ?
  - if dynamic, when to shrink ? when to stop shrink ?
define of start and end ?
freq dict or index dict ?


# Two Pointers
- should you sort list at first?
  - sorting the array will take O(n * logn)
- fast + slow or same speed
- start point:
  - bp03 starts at middle
- we curious at pointers'
  - value
    - swap or sum
  - position


# Fast & Slow Pointers
- linked list can be used at a looped chain scenario
- something related to: loop, middle (or 1/3, 1/4 etc.)

the time complexity of cp03 is very interesting


# Merge Intervals
4 merging scenarios
