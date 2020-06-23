-- https://leetcode-cn.com/problems/rank-scores/
-- Pre-uniqued version of ans3

SELECT score,

  (SELECT count(*)
   FROM
     (SELECT DISTINCT score s
      FROM scores) tmp
   WHERE s >= score) rank
FROM scores
ORDER BY score DESC