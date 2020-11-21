# Recursion
## Normal Recursion
    https://en.wikipedia.org/wiki/Recursion_(computer_science)/
    https://www.geeksforgeeks.org/recursion/
    https://www.geeksforgeeks.org/recursive-functions/
    https://www.geeksforgeeks.org/recursive-bubble-sort/

## Process
Example: 486-0

[1] a simple base case(s), not a terminating senario
[2] a set of rules: recurrence relation
[3] terminating senario

i.e.
[1] Base State
[2] State Transfer Equation
[3] Initialize Conditions
[4] Terminate Conditions

** Draw Recursice calls as a tree **
Think `top to bottom` when consider base state and state transfer
Recursive algorithms can be very space inefficient.
Each recursive call adds a new layer to the stack, which means that if your algorithm recurses to a depth of n, it uses at least O (n) memory.
All recursive algorithms can be implemented iteratively, sometimes the code to do so is much more complex.

## Types
[1] direct recursion
```cpp
int fact(int n)
{
    if (n < = 1) // base case
        return 1;
    else    
        return n*fact(n-1);    
}
```

[2] indirect recursion
```cpp
void indirectRecFun1()
{
    // Some code...
    indirectRecFun2();
    // Some code...
}
void indirectRecFun2()
{
    // Some code...
    indirectRecFun1();
    // Some code...
}
```

## Tail Recursion
https://www.geeksforgeeks.org/tail-recursion/
```cpp
void print(int n) 
{ 
    if (n < 0)  return; 
    cout << " " << n; 
  
    // The last executed statement is recursive call 
    print(n-1); 
} 
```
