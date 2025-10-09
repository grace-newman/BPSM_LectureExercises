#!/usr/bin/bash

# List the subject accession identification number for all of the high scoring segment
# pairs listed in the blastoutput2.out file.

	# The subject accession number is the second column of data. We will need to ignore the comment lines and then report the second coloumn of data.

rm -f *.exercise.out
goodlines=$(grep -v "#" ${inputfile} | wc -l | cut -d ' ' -f1)
unset IFS
unset dataline
shortHSP=0;
hspcounter=0;
echo -e "We have ${goodlines} data lines for processing... \n"

dupS_acc=() # Initialize a bash array for multiple HSPs

group1cut=150
group2cut=250
group3cut=350
outfile1="HSPscore.${group1cut}.exercise.out"
outfile2="HSPscore.${group2cut}.exercise.out"
outfile3="HSPscore.${group3cut}.exercise.out"
outfile4="HSPscore.morethan.${group3cut}.exercise.out"

rm -f ${outfile1} ${outfile2} ${outfile3} ${outfile4}

while read wholeline
do
# echo "Line is ${wholeline}"

if test ${wholeline:0:1} != "#"
then
dataline=$((dataline+1))
# echo "Line ${dataline} starts with ${wholeline:0:1}"

# Split the headings into the fields
read Q_acc S_acc pc_identity alignment_length mismatches gap_opens Q_start Q_end S_start S_end evalue bitscore <<< ${wholeline}

# Ensure the bitscore is an integer number and not a float by formating hte output using printf
bitscore=$(printf "%.0f\n" ${bitscore})

# List the subject accession lines for all high-scoring segment pairs
echo -e "${dataline}\t${Q_acc}\t${S_acc}" >> Subject_accessions.exercise.out

# List the alignment length and percent ID for all HSPs
echo -e "${dataline}\t${Q_acc}\t${alignment_length}\t${pc_identity}" >> al_length_pcID.exercise.out

# Show the HSPs with more than 20 mismatches
if test ${mismatches} -gt 20
then
echo -e "Line with more than 20 mismatches: ${dataline}\t${Q_acc}\tMismatches:\t${mismatches}"
fi

# Show the HSPs shorter than 100 amino acids and with more than 20 mismatches
if test ${alignment_length} -lt 100 && test ${mismatches} -gt 20
then
echo -e "HSPs shorter than 100 amino acids and with more than 20 mismatches: ${dataline}\t${Q_acc}\tLength: ${alignment_length}\tMismatches: ${mismatches}"
fi

# List the first 20 HSPs that have fewer than 20 mismatches
if test ${mismatches} -lt 20
then hspcounter=$((hspcounter+1))
if test ${hspcounter} -le 20
then
hsp_array+=${wholeline}
echo -e "${dataline}\t${hspcounter}\t${wholeline}" >> Fewer.than20MM.exercise.out
fi
fi

# How many HSPs are shorter than 100 amino acids
if test ${alignment_length} -lt 100
then shortHSP=$((shortHSP+1))
fi

# List the top 10 highest (best) HSPs
if test ${dataline} -le 10
then
echo -e "${dataline}\t${wholeline}" >> top10.HSPs.exercise.out
fi

# List the start positions of all matches where the HSP Subject accession includes the letters string "AEI"
if [[ ${S_acc} == *"AEI"* ]];
then
echo -e "${dataline}\tcontains AEI:\t${S_acc}. Subject starts at ${S_start}, Query starts at ${Q_start}" >> AEIinSubjectAcc.starts.exercise.out
fi

# How many subject sequences have more than one HSP
if test ${S_acc} == ${pre_acc}
then dupecount=$((dupecount+1))
if [[ dupecount == 1 ]]; then
dupS_acc=${S_acc}
fi
if [[ $dupS_acc == *${S_acc}* ]]; then
echo ""
else
dupS_acc+=(${S_acc})
fi
fi
pre_acc=${S_acc}

# What percentage of each HSP is made up of mismatches?
MM_percent=$((100*${mismatches}/${alignment_length}))
echo -e "${dataline}\tMismatch percent:\t${MM_percent}%" >>  Mismatchpercent.exercise.out

# Allocate HSPs into different groups based on their scores
scorebin=1
if [ ${bitscore} -gt ${group3cut} ]; then
scorebin=4
fi
if [ ${bitscore} -le ${group3cut} ] && [ ${bitscore} -gt ${group2cut} ]; then 
     scorebin=3
fi
if [ ${bitscore} -le ${group2cut} ] && [ ${bitscore} -gt ${group1cut} ]; then 
     scorebin=2
fi

scoregroupdetails=$(echo -e "${dataline}\t${Q_acc}\t${S_acc}\t${bitscore}")
case ${scorebin} in
4)
echo -e "${scoregroupdetails}" >> ${outfile4}
    ;;
  3)
    echo -e "${scoregroupdetails}" >> ${outfile3}
    ;;
  2)
    echo -e "${scoregroupdetails}" >> ${outfile2}
    ;;
  1)
    echo -e "${scoregroupdetails}" >> ${outfile1}
    ;;
esac

if test ${dataline} -eq ${goodlines}
then
echo -e "\n\nENDBLOCK\n\nThere were ${shortHSP} HSPs shorter than 100 amino acids"
echo -e "There were ${#dupS_acc[@]} Subjects with multiple HSPs"
fi
fi # was not a commented line in the blast data
done < ${inputfile}
