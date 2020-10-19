# Backtracking
    https://en.wikipedia.org/wiki/Backtracking/
    https://en.wikipedia.org/wiki/Eight_queens_puzzle/
    https://www.geeksforgeeks.org/backtracking-introduction/

Backtracking is an algorithm for finding *all solutions* by exploring all potential candidates (sudoku)
If the solution candidate turns to be not a solution (or at least not the last one), backtracking algorithm discards it by making some changes on the previous step, i.e. backtracks and then try again
Backtracking is an approach to solving constraint-satisfaction problems *without* trying all possibilities

In a backtracking, we need:
    [1] a simple base case(s) for recursion, not a terminating senario
    [2] a set of rules for backtrack ()
    [3] loop over remaining pieces, need a pointer to track the position

i.e.
[1] Base State

[2] State Transfer Equation

[3] Backtrack senario

[4] Initialize Conditions

[5] Terminate Conditions


## usage
There are three types of problems in backtracking 
- Decision Problem – In this, we search for a feasible solution.
- Optimization Problem – In this, we search for the best solution.
- Enumeration Problem – In this, we find all feasible solutions.

All items with duplicates need to be sorted before to ensure that there are no duplicates in the results


## Tamplate
LC077

Pseudo Code for Backtracking
[1] Recursive backtracking solution
```cpp
void findSolutions(n, other params) :
    if (found a solution) :
        solutionsFound = solutionsFound + 1;
        displaySolution();
        if (solutionsFound >= solutionTarget) : 
            System.exit(0);
        return

    for (val = first to last) :
        if (isValid(val, n)) :
            applyValue(val, n);
            findSolutions(n+1, other params);
            removeValue(val, n);
```

[2] Finding whether a solution exists or not
```cpp
bool findSolutions(n, other params) :
    if (found a solution) :
        displaySolution();
        return true;

    for (val = first to last) :
        if (isValid(val, n)) :
            applyValue(val, n);
            if (findSolutions(n+1, other params))
                return true;
            removeValue(val, n);
        return false;
```


## Backtracking vs DFS:
I would say, DFS is the special form of backtracking; backtracking is the general form of DFS.
Usually, a depth-first-search is a way of iterating through an actual graph/tree structure looking for a value, whereas backtracking is iterating through a problem space looking for a solution. Backtracking is a more general algorithm that doesn't necessarily even relate to trees.


## Backtracking vs DP:
    https://www.quora.com/q/loveforprogramming/Backtracking-Memoization-Dynamic-Programming
Dynamic programming is a method of solving complex problems by breaking them down into simpler steps. It is applicable to problems that exhibit the properties of 
  1) overlapping subproblems which are only slightly smaller
  2) optimal substructure


## Time Complexity
Hamiltonian cycle : O(N!) in the worst case  => factorial
WordBreak and StringSegment : O(2^N)  => exponential
NQueens : O(N!)


# lru_cache() [least recently used cache]
https://docs.python.org/3/library/functools.html
https://leetcode.com/problems/stone-game-ii/discuss/345230/Python-DP-Solution
An LRU (least recently used) cache works best when the most recent calls are the best predictors of upcoming calls
