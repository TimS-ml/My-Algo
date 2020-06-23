-- https://leetcode-cn.com/problems/rank-scores/
-- Var in MySQL: set @x1 += 7;
-- one for the current rank and one for the previous score
-- (@prev <> (@prev := Score) makesure they are not equal

SELECT score, @rank := @rank + (@prev <> (@prev := score)) rank
FROM scores,

  (SELECT @rank := 0, @prev := -1) init
ORDER BY score DESC