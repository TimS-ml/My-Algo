- [Day 1 - Advent of Code 2018](https://adventofcode.com/2018/day/1)
- [-🎄- 2018 Day 1 Solutions -🎄- : adventofcode](https://www.reddit.com/r/adventofcode/comments/a20646/2018_day_1_solutions/)

Consider this input:
+10000000
-9999999

Cumsum is:
0, 10000000, 1, 10000001, 2, 10000002, 3 ...

i.e. the shift value:
1st iter base val = 0
2nd iter base val = sum(input) = 1
3rd iter base val = sum(input) x 2 = 2

shift value list in the input:
10000000, 10000001, 10000002, 10000003...
1,        2,        3,        4

