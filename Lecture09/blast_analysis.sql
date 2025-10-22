select "### This is the output generated using the script blast_analysis.sql" AS '' ;
select "### Make a database "  AS '' ;
create database if not exists s2823303_exercises ;

select "### tell mysql we want to use this database" AS '' ;
use s2823303_exercises ;

select "### create a table with the right columns" AS '' ;
create table if not exists blasthits 
         (query text, subject text, pcid float, alignlen int, 
         mm int, gaps int, qstart int, qend int, substart int, 
         subend int, eval float, score float, HSP_group int) ;
truncate table blasthits ;

select "### load the data in from the file we have ready" AS '' ;
LOAD DATA local INFILE 
      '/home/s2823303/Exercises/Lecture09/blastoutput2.out_noheader' 
      INTO TABLE blasthits 
      FIELDS TERMINATED BY '\t' ;

select "### check the table structure" AS '' ;
describe blasthits ;

select "### show the HSPs with more than 20 mismatches" AS '' ;
select * from blasthits where mm > 20 ;

select "### show the HSPs shorter than 100 amino acids and with more than 20 mismatches" AS '' ;
select * from blasthits where mm > 20 and alignlen < 100 ;

select "### list the first 20 HSPs that have fewer than 20 mismatches" AS '' ;
select * from blasthits where mm < 20 limit 20 ;

select "### how many HSPs are shorter than 100 amino acids?" AS '' ;
select count(*) from blasthits where alignlen < 100 ;

select "### list the top ten highest (best) HSPs." AS '' ;
select * from blasthits order by score desc limit 10 ;

select "### list the start positions of all matches where the HSP Subject accession includes the letters string \"AEI\"" AS '' ;
select "### OPTED FOR SUBJECT START" AS '' ;
select substart from blasthits where subject like '%AEI%' ;

select "### how many subject sequences have more than one HSP?" AS '' ;
select "### Show rows of data, using a derived table" AS '' ;
select sub1,sub2
FROM (select subject as sub1, count(*) as sub2 from blasthits GROUP BY subject) AS sub
WHERE sub2 > 1 ;

select "### Show row count, using a derived table of a derived table!" AS '' ;
select count(*) from
(select sub1,sub2
FROM (select subject as sub1, count(*) as sub2 from blasthits GROUP BY subject) AS sub
WHERE sub2 > 1) AS FOO ;

select "### what percentage of each HSP is made up of mismatches?" AS '' ;
select 100 * mm / alignlen from blasthits ;

select "### allocate HSPs into different groups based on their scores" AS '' ;
select "### Add a column to the table to take our group number, default value 0" AS '' ;
select "### alter table blasthits add column HSP_group int default 0 ;" AS '' ;

select "### Now it is just a series of updates to values" AS '' ;
UPDATE blasthits SET HSP_group = 1 WHERE score < 100 ;
UPDATE blasthits SET HSP_group = 2 WHERE score >= 100 ;
UPDATE blasthits SET HSP_group = 3 WHERE score >= 200 ;
UPDATE blasthits SET HSP_group = 4 WHERE score >= 300 ;
UPDATE blasthits SET HSP_group = 5 WHERE score >= 400 ;

select "### We can also do a tally of the groups" AS '' ;
select HSP_group, count(*) from blasthits group by HSP_group ;

select "### All done!" AS '' ;

