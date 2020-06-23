-- https://leetcode-cn.com/problems/rising-temperature/

SELECT id
FROM
  (SELECT CASE
              WHEN temperature > @prevtemp
                   AND datediff(recorddate, @prevdate) = 1 THEN id
              ELSE NULL
          END AS id, @prevtemp:=temperature, @prevdate:=recorddate
   FROM weather,

     (SELECT @prevtemp:=NULL) AS a,

     (SELECT @prevdate:=NULL) AS b
   ORDER BY recorddate ASC) AS d
WHERE id IS NOT NULL