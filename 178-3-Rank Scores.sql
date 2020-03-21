-- https://leetcode-cn.com/problems/rank-scores/
-- This one counts for each score, the number of distinct greater or equal scores.

select Score,
  (select count(distinct Score)
   from Scores
   where Score >= s.Score) Rank
from Scores s
order by Score desc;