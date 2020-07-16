```
     ___          _        __           __  _____        __
 __ / (_)__ ____ ( )___   / /  ___ ___ / /_/ ___/__  ___/ /__
/ // / / _ `/ _ \|/(_-<  / /__/ -_) -_) __/ /__/ _ \/ _  / -_)
\___/_/\_,_/_//_/ /___/ /____/\__/\__/\__/\___/\___/\_,_/\__/
```


# How to Practice

```
https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=521825

“把周赛当作模拟面试，是能够很好检测你刷题水平的方式”


一開始我刷的很慢，因為每一條我只少想兩個方法做，所以一天只能3,4條新medium。之後快了，也只能6條新左右。

刷題多少不是重點，重點是：

[1] presentation。特別是在phonein時，要講得讓interviewer明白
[2] 要能在不用editor/compilor幫助下，写(尽量)bug-free的code。因為不論是whiteboard還是phonein用google doc/livecode/coderpad，你不會有editor/compiler幫助，interviwer也不會幫你debug

所以現在，每題我也像考speaking般:

[1] 先說thought prcoess
[2] 後說testcases
  -> 說的時候我會在紙上寫code
  -> 說完之後直接寫到刷題網站submit

P.S.1 現在一天：兩條新題，6-8條舊題。我共刷了500左右，不過我覺得常見的只有100-200條
P.S.1 除了刷題網，我最近玩google code jam(今天5pm round 1C)及google kick start當練習。這些比難度大約medium->hard，而且time limit 3小時3-4題，十分適合當mock interview

我不清楚其他高手怎練，但我這樣練拿final interview的機率高了，希望未來幾星期pass吧

```



# Formating 
[0] Code name
In `CodeList.md`:

H076 = mark+rev means this is a hard question, tag = mark and review


[1] C++ format
```
clang-format -i -style=LLVM *.cpp

clang-format -i path/to/electron/file.cpp -style=LLVM

clang-format -i main.cpp -style=LLVM
```
