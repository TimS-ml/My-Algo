-- https://leetcode-cn.com/problems/combine-two-tables/

/* Create Table
Create table Person (PersonId int, FirstName varchar(255), LastName varchar(255));
Create table Address (AddressId int, PersonId int, City varchar(255), State varchar(255));

insert into Person (PersonId, LastName, FirstName) values ('1', 'Wang', 'Allen');
insert into Address (AddressId, PersonId, City, State) values ('1', '2', 'New York City', 'New York');
*/

/* Test Case
Truncate table Person;
Truncate table Address;
insert into Person (PersonId,LastName,FirstName) values('1','Wang','Allen');
insert into Address (AddressId,PersonId,City,State) values('1','2','New York City','New York');
*/


select FirstName, LastName, City, State
from Person left join Address 
on Person.PersonId = Address.PersonId;

/* or
select FirstName, LastName, City, State
from Person left join Address 
using(PersonId);
*/

