-- https://leetcode-cn.com/problems/average-selling-price/

-- Create table If Not Exists Prices (product_id int, start_date date, end_date date, price int);
-- Create table If Not Exists UnitsSold (product_id int, purchase_date date, units int);

-- insert into Prices (product_id, start_date, end_date, price) values ('1', '2019-02-17', '2019-02-28', '5');
-- insert into Prices (product_id, start_date, end_date, price) values ('1', '2019-03-01', '2019-03-22', '20');
-- insert into Prices (product_id, start_date, end_date, price) values ('2', '2019-02-01', '2019-02-20', '15');
-- insert into Prices (product_id, start_date, end_date, price) values ('2', '2019-02-21', '2019-03-31', '30');

-- insert into UnitsSold (product_id, purchase_date, units) values ('1', '2019-02-25', '100');
-- insert into UnitsSold (product_id, purchase_date, units) values ('1', '2019-03-01', '15');
-- insert into UnitsSold (product_id, purchase_date, units) values ('2', '2019-02-10', '200');
-- insert into UnitsSold (product_id, purchase_date, units) values ('2', '2019-03-22', '30');

select P.product_id, round(SUM(U.units * P.price) / SUM(U.units), 2) as average_price
from UnitsSold U, Prices P
where P.product_id = U.product_id
and P.start_date <= U.purchase_date
and P.end_date >= U.purchase_date
group by product_id