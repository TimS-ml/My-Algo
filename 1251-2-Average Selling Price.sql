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

SELECT p.product_id,
       round(sum(u.units * p.price) / sum(u.units), 2) AS average_price
FROM unitssold u,
     prices p
WHERE p.product_id = u.product_id
  AND p.start_date <= u.purchase_date
  AND p.end_date >= u.purchase_date
GROUP BY product_id