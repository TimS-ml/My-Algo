# Recursion
## Normal Recursion
    https://en.wikipedia.org/wiki/Recursion_(computer_science)/
    https://www.geeksforgeeks.org/recursion/
    https://www.geeksforgeeks.org/recursive-functions/
    https://www.geeksforgeeks.org/recursive-bubble-sort/

In a recursive, we need:
    [1] a simple base case(s), not a terminating senario
    [2] a set of rules: recurrence relation
    [3] terminating senario

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
