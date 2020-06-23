-- https://leetcode-cn.com/problems/reformat-department-table/
 /*
Create table If Not Exists Department (id int, revenue int, month varchar(5));

insert into Department (id, revenue, month) values ('1', '8000', 'Jan');
insert into Department (id, revenue, month) values ('2', '9000', 'Jan');
insert into Department (id, revenue, month) values ('3', '10000', 'Feb');
insert into Department (id, revenue, month) values ('1', '7000', 'Feb');
insert into Department (id, revenue, month) values ('1', '6000', 'Mar');
*/
SELECT id,
       sum(CASE
               WHEN MONTH = 'jan' THEN revenue
               ELSE NULL
           END) AS jan_revenue,
       sum(CASE
               WHEN MONTH = 'feb' THEN revenue
               ELSE NULL
           END) AS feb_revenue,
       sum(CASE
               WHEN MONTH = 'mar' THEN revenue
               ELSE NULL
           END) AS mar_revenue,
       sum(CASE
               WHEN MONTH = 'apr' THEN revenue
               ELSE NULL
           END) AS apr_revenue,
       sum(CASE
               WHEN MONTH = 'may' THEN revenue
               ELSE NULL
           END) AS may_revenue,
       sum(CASE
               WHEN MONTH = 'jun' THEN revenue
               ELSE NULL
           END) AS jun_revenue,
       sum(CASE
               WHEN MONTH = 'jul' THEN revenue
               ELSE NULL
           END) AS jul_revenue,
       sum(CASE
               WHEN MONTH = 'aug' THEN revenue
               ELSE NULL
           END) AS aug_revenue,
       sum(CASE
               WHEN MONTH = 'sep' THEN revenue
               ELSE NULL
           END) AS sep_revenue,
       sum(CASE
               WHEN MONTH = 'oct' THEN revenue
               ELSE NULL
           END) AS oct_revenue,
       sum(CASE
               WHEN MONTH = 'nov' THEN revenue
               ELSE NULL
           END) AS nov_revenue,
       sum(CASE
               WHEN MONTH = 'dec' THEN revenue
               ELSE NULL
           END) AS dec_revenue
FROM department
GROUP BY id
ORDER BY id;

/* or (this is faster)
    max(if(month = 'Jan', revenue, null)) AS Jan_Revenue,
    max(if(month = 'Feb', revenue, null)) AS Feb_Revenue,
    max(if(month = 'Mar', revenue, null)) AS Mar_Revenue,
    max(if(month = 'Apr', revenue, null)) AS Apr_Revenue,
    max(if(month = 'May', revenue, null)) AS May_Revenue,
    max(if(month = 'Jun', revenue, null)) AS Jun_Revenue,
    max(if(month = 'Jul', revenue, null)) AS Jul_Revenue,
    max(if(month = 'Aug', revenue, null)) AS Aug_Revenue,
    max(if(month = 'Sep', revenue, null)) AS Sep_Revenue,
    max(if(month = 'Oct', revenue, null)) AS Oct_Revenue,
    max(if(month = 'Nov', revenue, null)) AS Nov_Revenue,
    max(if(month = 'Dec', revenue, null)) AS Dec_Revenue
*/