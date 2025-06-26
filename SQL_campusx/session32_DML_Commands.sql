use campus_study;
show tables;
select * from smartphones;
desc smartphones;

select model,battery_capacity from smartphones;

-- alias : renaming the colums
select os as "Operating System", battery_capacity as "Mahh" from smartphones order by Mahh ASC;


-- calculatin the ppi

select model , sqrt(resolution_width*resolution_width + resolution_height*resolution_height)/screen_size as "PPI" from smartphones;

-- constants
select model,"smartphone" AS "Type" from smartphones;

-- Distinct
select count(distinct brand_name) from smartphones;  -- this will giev the count of all brand names present in the tables

select distinct os as "Operating System " from smartphones;

select distinct brand_name, processor_brand from smartphones order by brand_name ;

-- filtering rows based on where clause

-- find smartphoens where price >15000 and smarphones = samsung
select brand_name,price from smartphones where brand_name="samsung" and price>15000;

-- phoen wtiht price>50000
select * from smartphones where price>50000;
select count(distinct brand_name) from smartphones where price>50000; 

-- between
--  find all phones in range of 10000 and 20000
select * from smartphones where price between 10000 and 20000 order by price;


-- rating>80 and price 25000
select * from smartphones where price<25000 and rating>80;


--  find samsunf where ram >8 gb
select * from smartphones where brand_name= "samsung" and processor_brand="snapdragon" and ram_capacity >=8;


-- Query execution order 
-- F J W G H S D O
-- from join where groupby having select distinct orderby
-- this is the order in which query is get executed 


 -- select brand_name who sell smartphoens with price>50000;
select brand_name from smartphones where price>50000;


-- IN and NOT IN 
select * from smartphones where processor_brand="snapdragon" or processor_brand="bionic";
-- another way for above query
select * from smartphones where processor_brand in ('snapdragon','bionic');


--  update 
update smartphones set processor_brand="dimensity" where processor_brand="mediatek";
select * from smartphones where processor_brand="dimensity";

-- delete query to delete the rows

--  delete smartphones where price >2000000 as they are outliers
delete from smartphones where price>2000000;

-- based on multiple condition
delete from smartphones where primary_camera_rear >150 and brand_name="samsung";

--  aggregation funciton in sql

select max(price) from smartphones;

select min(price)from smartphones;

select avg(price) from smartphones where brand_name="apple";

-- find the no of one plus phones
select count(*) from smartphones where brand_name="oneplus";

select count(distinct brand_name) from smartphones;

-- STD
select STD(screen_size) from smartphones;

select variance(screen_size) from smartphones;


-- scalar functions 
--  ABS

select price-100000 as "temp" from smartphones;

select abs( price-100000) as "temp" from smartphones;



--  round
select model, round(sqrt(resolution_width*resolution_width + resolution_height*resolution_height)/screen_size ) as "PPI" from smartphones;

--  ceil and floor
-- 4.1-> 5 karel ceil
-- 4.1 la 4 karel floor
select ceil(screen_size) from smartphones;



-- some questions for practice given by sir
--  find the average battery_capacity and the average primary rear camera resolution for all the smartphones with price greater than or equal to 100000
select avg(battery_capacity) as "Average Battery Capacity", avg(primary_camera_rear) as "Average resolution"  from smartphones where price>=100000;

select * from smartphones;

select avg(internal_memory) from smartphones where refresh_rate = 120 and primary_camera_front >= 20;


select count(brand_name) from smartphones where has_5g = 'True' ;







