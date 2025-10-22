#!/usr/bin/sql

-- List the accession numbers of hits that belong to humans
SELECT
    sample_table.sample_id,
    sequence_table.sequence_id,
    sample_table.common_name,
    hit_table.accession
FROM sample_table
JOIN sequence_table
    ON sample_table.sample_id = sequence_table.sample_id
JOIN hit_table
    ON sequence_table.sequence_id = hit_table.sequence_id
WHERE sample_table.common_name = 'human';


-- List all the sequences with longer than 700 bases
select sequence from blast_table where length > 700;

-- List the common names and species names for all samples
select common_name, scientific_name from blast_table;

-- List the accession numbers of hits whose length and score are both greater than 100
select hit_accession from blast_table where hit_length > 100 and hit_score > 100;

-- List the DNA of the sequences which have a hit whose score and length are both greater than 100
select sequence from blast_table where hit_length > 100 and hit_score > 100;
