Only the python solution contains the time complexity stuffs
For problem set:
- write down thought process first
  - update which part stacked
- this problem is similar to which example problems

# Plan
Pattern and thought process
Tamplate


# [a] Sliding Window
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


# [b] Two Pointers
- should you sort list at first?
  - sorting the array will take O(n * logn)
- fast + slow or same speed
- start point:
  - bp03 starts at middle
- we curious at pointers'
  - value
    - swap or sum
  - position


# [c] Fast & Slow Pointers
- linked list can be used at a looped chain scenario
- something related to: loop, middle (or 1/3, 1/4 etc.)

the time complexity of cp03 is very interesting


# [d] Merge Intervals
4 merging scenarios


# [e] Cyclic Sort


# [f] In-place Reversal of a LinkedList


# [g] Tree Breadth First Search


# [h] Tree Depth First Search


# [i] Two Heaps


# [j] Subsets


# [k] Modified Binary Search


# [l] Bitewise XOR
LC 050

Bitwise operators
https://www.rapidtables.com/convert/number/decimal-to-binary.html
https://en.wikipedia.org/wiki/Bitwise_operation
https://wiki.python.org/moin/BitwiseOperators
AND: &
OR : |
XOR: ^
Invert/complement: ~

Remember the important property of XOR that it returns 0 if both the bits in comparison are the same. 

binary to decimal:
int(binary, a)

decimal to binary:
'{0:b}'.format(a)

## Important properties of XOR to remember
Taking XOR of a number with itself returns 0, e.g.,
1 ^ 1 = 0
29 ^ 29 = 0

Taking XOR of a number with 0 returns the same number, e.g.,
1 ^ 0 = 1
31 ^ 0 = 31

XOR is Associative & Commutative, which means:
(a ^ b) ^ c = a ^ (b ^ c)
a ^ b = b ^ a


# [m] Top 'K' Elements


# [n] K-way merge


# [o] 0/1 Knapsack (DYnamic Programming)
https://en.wikipedia.org/wiki/Knapsack_problem
After the `recursive` solution, we will modify our algorithm to apply advanced techniques of `Memoization` and `Bottom-Up Dynamic Programming` to develop a complete understanding of this pattern.
Draw the state tree can help you solve DP


# [p] Topological Sort (Graph)
https://en.wikipedia.org/wiki/Topological_sorting
https://blog.csdn.net/lisonglisonglisong/article/details/45543451
Generally, a directed acyclic graph can have one or more topological sorting sequences. (that's why in `pp01` it mentioned: every directed edge (U, V) from vertex U to vertex V, U comes before V in the ordering.)

