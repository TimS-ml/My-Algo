-- https://leetcode-cn.com/problems/students-and-examinations/
 -- Create table If Not Exists Students (student_id int, student_name varchar(20))
-- Create table If Not Exists Subjects (subject_name varchar(20))
-- Create table If Not Exists Examinations (student_id int, subject_name varchar(20))
 -- Truncate table Students
-- insert into Students (student_id, student_name) values ('1', 'Alice')
-- insert into Students (student_id, student_name) values ('2', 'Bob')
-- insert into Students (student_id, student_name) values ('13', 'John')
-- insert into Students (student_id, student_name) values ('6', 'Alex')
 -- Truncate table Subjects
-- insert into Subjects (subject_name) values ('Math')
-- insert into Subjects (subject_name) values ('Physics')
-- insert into Subjects (subject_name) values ('Programming')
 -- Truncate table Examinations
-- insert into Examinations (student_id, subject_name) values ('1', 'Math')
-- insert into Examinations (student_id, subject_name) values ('1', 'Physics')
-- insert into Examinations (student_id, subject_name) values ('1', 'Programming')
-- insert into Examinations (student_id, subject_name) values ('2', 'Programming')
-- insert into Examinations (student_id, subject_name) values ('1', 'Physics')
-- insert into Examinations (student_id, subject_name) values ('1', 'Math')
-- insert into Examinations (student_id, subject_name) values ('13', 'Math')
-- insert into Examinations (student_id, subject_name) values ('13', 'Programming')
-- insert into Examinations (student_id, subject_name) values ('13', 'Physics')
-- insert into Examinations (student_id, subject_name) values ('2', 'Math')
-- insert into Examinations (student_id, subject_name) values ('1', 'Math')
 -- select *
-- from Students a cross join Subjects b
--     left join Examinations e on a.student_id = e.student_id and b.subject_name = e.subject_name
 -- Use COUNT(e.subject_name) for the reason that e.subject_name has NULL

SELECT a.student_id,
       a.student_name,
       b.subject_name,
       count(e.subject_name) AS attended_exams
FROM students a
CROSS JOIN subjects b
LEFT JOIN examinations e ON a.student_id = e.student_id
AND b.subject_name = e.subject_name
GROUP BY a.student_id,
         b.subject_name
ORDER BY a.student_id,
         b.subject_name