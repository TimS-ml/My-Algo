-- https://leetcode-cn.com/problems/combine-two-tables/

CREATE TABLE
CREATE TABLE person (personid int, firstname varchar(255),
                                             lastname varchar(255));


CREATE TABLE address (addressid int, personid int, city varchar(255),
                                                        state varchar(255));


INSERT INTO person (personid, lastname, firstname)
VALUES ('1', 'Wang', 'Allen');


INSERT INTO address (addressid, personid, city, state)
VALUES ('1', '2', 'New York City', 'New York');

test CASE TRUNCATE TABLE person;

TRUNCATE TABLE address;


INSERT INTO person (personid, lastname, firstname)
VALUES('1','Wang','Allen');


INSERT INTO address (addressid, personid, city, state)
VALUES('1','2','New York City','New York');


SELECT firstname,
       lastname,
       city,
       state
FROM person
LEFT JOIN address ON person.personid = address.personid;

--  or

SELECT firstname,
       lastname,
       city,
       state
FROM person
LEFT JOIN address USING(personid);

