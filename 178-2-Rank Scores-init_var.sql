-- https://leetcode-cn.com/problems/rank-scores/
-- Var in MySQL: set @x1 += 7;
-- one for the current rank and one for the previous score
-- (@prev <> (@prev := Score) makesure they are not equal

select Score, @rank := @rank + (@prev <> (@prev := Score)) Rank
from Scores,
  (select @rank := 0, @prev := -1) init
order by Score desc