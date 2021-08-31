-- https://leetcode-cn.com/problems/rank-scores/
-- If there is a tie between two scores, both should have the same ranking
-- Note that after a tie, the next ranking number should be the next consecutive integer value.

SELECT scores.score,
       count(ranking.score) AS rank
FROM scores,

  (SELECT DISTINCT score
   FROM scores) ranking
WHERE scores.score <= ranking.score
GROUP BY scores.id,
         scores.score
ORDER BY scores.score DESC;


SELECT s.score,
       count(DISTINCT t.score) rank
FROM scores s
JOIN scores t ON s.score <= t.score
GROUP BY s.id
ORDER BY s.score DESC


-- Var in MySQL: set @x1 += 7;
-- one for the current rank and one for the previous score
-- (@prev <> (@prev := Score) makesure they are not equal

SELECT score, @rank := @rank + (@prev <> (@prev := score)) rank
FROM scores,

  (SELECT @rank := 0, @prev := -1) init
ORDER BY score DESC


-- This one counts for each score, the number of distinct greater or equal scores.
SELECT score,

  (SELECT count(DISTINCT score)
   FROM scores
   WHERE score >= s.score) rank
FROM scores s
ORDER BY score DESC;

-- Pre-uniqued version
SELECT score,

  (SELECT count(*)
   FROM
     (SELECT DISTINCT score s
      FROM scores) tmp
   WHERE s >= score) rank
FROM scores
ORDER BY score DESC
