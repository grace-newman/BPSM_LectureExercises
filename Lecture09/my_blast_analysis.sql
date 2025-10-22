-- My blast analysis SQL script for the Lecture 09 Exercises

-- Show HSPs with more than 20 mismatches
select * from blasthits where mm > 20;

-- Show the HSPs shorter than 100 amino acids and with more than 20 mismatches
select * from blasthits where alignlen < 100 and mm > 20;

-- List the first 20 HSPs that have fewwer than 20 mismatches
select * from blasthits where mm < 20 limit 20;

-- How many HSPs are shorter than 100 amino acids?
select count(*) from blasthits where alignlen < 100;

-- List the top 10 highest (best) HSPs
select * from blasthits order by score desc limit 10;

-- List the start positions of all matches where the HSP Subject accession includes the letters string "AEI"
select substart from blasthits where subject like '%AEI%';

-- How many subject sequences have more than one HSP
select sub1,sub2
FROM (select subject as sub1, count(*) as sub2 from blasthits GROUP BY subject) AS sub
WHERE sub2 > 1;

select count(*) from
(select sub1,sub2
FROM (select subject as sub1, count(*) as sub2 from blasthits GROUP BY subject) AS sub
WHERE sub2 > 1) AS FOO ;

-- What percentage of each HSP is made up of mismatches?
select 100 * mm / alignlen from blasthits;

-- Allocate HSPs into different groups based on their scores and group them
select HSP_group, count(*) from blasthits group by HSP_group;

