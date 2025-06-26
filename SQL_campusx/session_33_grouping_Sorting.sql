use campus_study;
select * from smartphones;




-- find the  top 5 smartphones having bigger screen size;
select model,screen_size from smartphones order by screen_size DESC limit 5;

-- sorting is mainly used to sort the data for a particular condition


-- sort all the phones in desc order as per the no of total camera;
select model,  (num_rear_cameras + num_front_cameras) as "Total_cameras" from smartphones order by Total_cameras desc;


-- sort the data on basis of ppi in the decreasing order

select model , sqrt(resolution_width*resolution_width + resolution_height*resolution_height)/screen_size as "PPI" from smartphones order by PPI desc;

-- find the phone with 2nd largest battery

select model, battery_capacity from smartphones order by battery_capacity desc  LIMIT 1 OFFSET 1;

-- LIMIT 1 OFFSET 1: Skips the largest battery (OFFSET 1) and selects the second-largest battery (LIMIT 1).

-- find the name and rating of the worst rated apple phones
select model , rating from smartphones where brand_name="apple" order by rating limit 1;

--  sort phones alphabetically and then basis of rating
select * from smartphones order by brand_name asc ,rating desc;


-- grouping data : 

-- group smarthons by brand and get count , average orice , max_Rating avg scrren size and battery capacity 

select count(*),brand_name, avg(price), max(rating),avg(screen_size), avg(battery_capacity) from smartphones group by brand_name;


-- group smartphones by whether they have an NFC and get averagbe price and rating
select has_nfc ,avg(price), avg(rating) from smartphones group by has_nfc;


-- select avg(price), avg(rating),brand_name from smartphones where has_nfc = "True" group by brand_name;




-- group smartphones by the extended memory available and get the average price;

select extended_memory_available, avg(price) from smartphones group by extended_memory_available;


-- group smartphones by their brand_name and processor brand and get the count of models and the avergae primary camera resolution 
select brand_name,processor_brand ,count(model) from smartphones group by brand_name, processor_brand;


-- find the top 5 most costly smartphone brands

select brand_name ,avg(price) from smartphones group by brand_name  order by avg(price) desc limit 5;


--  which brand makes smallest screen size
select brand_name ,avg(screen_size) from smartphones group by brand_name  order by avg(screen_size) asc limit 1;

-- group smartphones by brand and find the brand with the highest no of model that have both nfc and IR blaster

select brand_name , count(*) from smartphones where has_nfc="True" and has_ir_blaster="True" group by brand_name ;


--  find all samsung 5g enaled smartphones and find out the average price for nf
select has_nfc,avg(price) from smartphones where brand_name="samsung" group by has_nfc;
 