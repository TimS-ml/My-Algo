-- https://leetcode-cn.com/problems/rank-scores/
-- This one counts for each score, the number of distinct greater or equal scores.

SELECT score,

  (SELECT count(DISTINCT score)
   FROM scores
   WHERE score >= s.score) rank
FROM scores s
ORDER BY score DESC;