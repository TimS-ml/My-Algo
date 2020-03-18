-- https://leetcode-cn.com/problems/reformat-department-table/

/*
Create table If Not Exists Department (id int, revenue int, month varchar(5));

insert into Department (id, revenue, month) values ('1', '8000', 'Jan');
insert into Department (id, revenue, month) values ('2', '9000', 'Jan');
insert into Department (id, revenue, month) values ('3', '10000', 'Feb');
insert into Department (id, revenue, month) values ('1', '7000', 'Feb');
insert into Department (id, revenue, month) values ('1', '6000', 'Mar');
*/

select id, 
	sum(case when month = 'jan' then revenue else null end) as Jan_Revenue,
	sum(case when month = 'feb' then revenue else null end) as Feb_Revenue,
	sum(case when month = 'mar' then revenue else null end) as Mar_Revenue,
	sum(case when month = 'apr' then revenue else null end) as Apr_Revenue,
	sum(case when month = 'may' then revenue else null end) as May_Revenue,
	sum(case when month = 'jun' then revenue else null end) as Jun_Revenue,
	sum(case when month = 'jul' then revenue else null end) as Jul_Revenue,
	sum(case when month = 'aug' then revenue else null end) as Aug_Revenue,
	sum(case when month = 'sep' then revenue else null end) as Sep_Revenue,
	sum(case when month = 'oct' then revenue else null end) as Oct_Revenue,
	sum(case when month = 'nov' then revenue else null end) as Nov_Revenue,
	sum(case when month = 'dec' then revenue else null end) as Dec_Revenue
from Department
group by id
order by id;

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
